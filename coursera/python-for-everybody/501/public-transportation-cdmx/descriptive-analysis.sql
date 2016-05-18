-- Total number of routes
SELECT COUNT(route_id) AS n_routes
FROM ROUTES;

-- Number of routes per agency
SELECT agency_id AS agency, COUNT(route_id) AS n_routes
FROM ROUTES
GROUP BY agency_id
ORDER BY n_routes DESC;

-- Number of routes per route type
SELECT route_type, COUNT(route_id) AS n_routes
FROM ROUTES
GROUP BY route_type
ORDER BY n_routes DESC;

-- Top ten routes with highest/lowest number of trips
SELECT TRIPS.route_id AS id, ROUTES.route_long_name AS route_name, 
	ROUTES.agency_id AS agency, COUNT(TRIPS.trip_id) AS n_trips
FROM TRIPS LEFT JOIN ROUTES
ON TRIPS.route_id = ROUTES.route_id
GROUP BY id
ORDER BY n_trips DESC -- Comment the 'DESC' parameter if you want top ten lowest
LIMIT 10;

-- Top ten services grouped by number of trips
-- SELECT SUM(TABLA_MAGICA.n_trips) -- Remove comments to verify the total number of trips with the TRIPS table's row
-- FROM (
	SELECT TRIPS_BY_SERVICE.service_id, TRIPS_BY_SERVICE.route_name, TRIPS_BY_SERVICE.agency, 
	CALENDAR.monday, CALENDAR.tuesday, CALENDAR.wednesday, CALENDAR.thursday, 
	CALENDAR.friday, CALENDAR.saturday, CALENDAR.sunday, 
	CALENDAR.monday + CALENDAR.tuesday + CALENDAR.wednesday + CALENDAR.thursday + CALENDAR.friday + CALENDAR.saturday + CALENDAR.sunday AS n_day, 
	TRIPS_BY_SERVICE.n_trips
	FROM (
		SELECT TRIPS.service_id, ROUTES.route_long_name AS route_name, 
			ROUTES.agency_id AS agency, COUNT(TRIPS.trip_id) AS n_trips
		FROM TRIPS LEFT JOIN ROUTES
		ON TRIPS.route_id = ROUTES.route_id
		GROUP BY service_id
		ORDER BY n_trips DESC) AS TRIPS_BY_SERVICE  LEFT JOIN CALENDAR
	ON TRIPS_BY_SERVICE.service_id = CALENDAR.service_id --) AS NTRIPS_BY_SERVICE