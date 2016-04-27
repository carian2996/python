import sqlite3
import csv
from time import sleep

conn = sqlite3.connect('transport-cdmx.sqlite')
conn.text_factory = str
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Routes 
    (route_id INTEGER PRIMARY KEY, agency_id TEXT, route_short_name TEXT, 
     route_long_name TEXT, route_desc TEXT, route_type INTEGER, route_url TEXT, 
     route_color TEXT, route_text_color TEXT, route_bike INTEGER)''')

with open('data/cdmx_gtfs/routes.txt') as routes_file:
	reader = csv.reader(routes_file)
	next(routes_file)
	for row in reader:
		row[4] = int(row[4]) # Converting to Integer
		row[8] = int(row[8]) 
		row[9] = int(row[9].split('_')[1]) 
		
		cursor.execute('''
			INSERT INTO Routes (agency_id, route_short_name, 
			route_long_name, route_desc, route_type, route_url, 
			route_color, route_text_color, route_bike, route_id) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)

conn.commit()

print "Process completed"