import sqlite3
import csv
from time import sleep

conn = sqlite3.connect('transport-cdmx.sqlite')
conn.text_factory = str
cursor = conn.cursor()

cursor.executescript('''

	DROP TABLE IF EXISTS ROUTES;
	DROP TABLE IF EXISTS TRIPS;
	DROP TABLE IF EXISTS STOPTIMES;
	DROP TABLE IF EXISTS STOPS;
	DROP TABLE IF EXISTS CALENDAR;

	CREATE TABLE ROUTES (
		route_id 			INTEGER PRIMARY KEY, 
		agency_id 			TEXT, 
		route_short_name 	TEXT, 
		route_long_name 	TEXT, 
		route_desc 			TEXT, 
		route_type 			INTEGER, 
		route_url 			TEXT, 
		route_color 		TEXT, 
		route_text_color 	TEXT, 
		route_bike 			INTEGER
	);

    CREATE TABLE TRIPS (
    	trip_id 			INTEGER PRIMARY KEY, 
    	route_id 			INTEGER, 
    	service_id 			INTEGER, 
    	trip_short_name 	TEXT, 
    	trip_desc 			TEXT, 
    	trip_headsign 		TEXT, 
    	route_short_name 	TEXT, 
    	direction_id 		TEXT,
    	block_id 			TEXT, 
    	shape_id 			INTEGER, 
    	wheelchair_access 	INTEGER, 
    	bikes_access 		INTEGER
    );

    CREATE TABLE STOPTIMES (
    	trip_sequence_id 	INTEGER, 
    	stop_id 			INTEGER, 
    	arrival_time 		TEXT, 
    	departure_time	 	TEXT, 
    	stop_headsign 		TEXT, 
    	route_short_name 	TEXT, 
    	pickup_type 		INTEGER, 
    	drop_off_type 		INTEGER,
    	shape_dist_traveled TEXT,
    	PRIMARY KEY (trip_sequence_id, stop_id)
    );

    CREATE TABLE STOPS (
    	stop_id 			INTEGER PRIMARY KEY, 
    	stop_code 			TEXT, 
    	stop_name 			TEXT, 
    	stop_desc 			TEXT, 
    	stop_lat		 	REAL, 
    	stop_lon	 		REAL, 
    	zone_id			 	TEXT, 
    	stop_url	 		TEXT,
    	location_type 		INTEGER, 
    	parent_station 		TEXT, 
    	wheelchair_access 	INTEGER, 
    	stop_direction 		TEXT
    );

	CREATE TABLE CALENDAR (
    	service_id 			INTEGER PRIMARY KEY, 
    	monday	 			INTEGER, 
    	tuesday 			INTEGER, 
    	wednesday 			INTEGER, 
    	thursday		 	INTEGER, 
    	friday		 		INTEGER, 
    	saturday			INTEGER, 
    	sunday		 		INTEGER,
    	start_data 			TEXT, 
    	end_date 			TEXT
    )    

''')

with open('data/cdmx_gtfs/routes.txt') as routes:
	reader = csv.reader(routes)
	next(routes)
	for row in reader:
		row[4] = int(row[4]) # Converting to Integer
		row[8] = int(row[8]) 
		row[9] = int(row[9].split('_')[1]) 
		
		cursor.execute('''
			INSERT INTO ROUTES (agency_id, route_short_name, 
			route_long_name, route_desc, route_type, route_url, 
			route_color, route_text_color, route_bike, route_id) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
conn.commit()
print 'Routes stored in database'
sleep(1)

with open('data/cdmx_gtfs/trips.txt') as trips:
	reader = csv.reader(trips)
	next(trips)
	for row in reader:
		row[0] = int(row[0].split('_')[1]) # Converting to Integer
		row[1] = int(row[1]) 
		row[8] = int(row[8]) 
		row[11] = int(row[11]) 
		
		cursor.execute('''
			INSERT INTO TRIPS (route_id, service_id, trip_short_name, 
			trip_desc, trip_headsign, route_short_name, direction_id, 
			block_id, shape_id, wheelchair_access, bikes_access, trip_id) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
conn.commit()
print 'Trips stored in database'
sleep(1)

with open('data/cdmx_gtfs/stop_times.txt') as stop_times:
	reader = csv.reader(stop_times)
	next(stop_times)
	for row in reader:
		if int(row[1]) < 10: row[1] = '0' + row[1]
		trip_sequence = int(row[0] + row[1])

		row[2] = int(row[2].split('_')[1])
		row[7] = int(row[7]) 
		row[8] = int(row[8])  

		to_db = row[2:]
		to_db.append(trip_sequence)

		cursor.execute('''
			INSERT INTO STOPTIMES (stop_id, arrival_time, departure_time, 
			stop_headsign, route_short_name, pickup_type, drop_off_type, 
			shape_dist_traveled, trip_sequence_id) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', to_db)
conn.commit()
print 'Stop times stored in database'
sleep(1)

with open('data/cdmx_gtfs/stops.txt') as stops:
	reader = csv.reader(stops)
	next(stops)
	for row in reader:
		row[0] = int(row[0].split('_')[1]) # Converting to Integer
		row[4] = float(row[4]) 
		row[5] = float(row[5]) 
		row[8] = int(row[8]) 
		row[10] = int(row[10]) 

		cursor.execute('''
			INSERT INTO STOPS (stop_id, stop_code, stop_name, stop_desc, 
			stop_lat, stop_lon, zone_id, stop_url, location_type, 
			parent_station, wheelchair_access, stop_direction)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
conn.commit()
print 'Stops stored in database'
sleep(1)

with open('data/cdmx_gtfs/calendar.txt') as calendar:
	reader = csv.reader(calendar)
	next(calendar)
	for row in reader:
		row[:8] = [int(x) for x in row[:8]]

		cursor.execute('''
			INSERT INTO CALENDAR (service_id, monday, tuesday, wednesday, 
			thursday, friday, saturday, sunday, start_data, end_date)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
conn.commit()
print 'Calendar stored in database'
sleep(1)

print "Process completed"