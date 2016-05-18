READ ME PLEASE
==============

This repo is used to create a basic database and visualization for public transportation data from Mexico City. The data is open in the following link: [Public Data](http://s3.amazonaws.com/setravi/df_gtfs.zip).

The zip files contain several files with a **GTFS format** (General Transit Feed Specification), *you can find more information about* _**GTFS format**_ *here:* [What is GTFS](http://developers.google.com/transit/gtfs/?hl=en).

## Data

* agency.txt - **Required** - One or more transit agencies that provide the data in this feed.
* calendar.txt - **Required** - Dates for service IDs using a weekly schedule. Specify when service starts and ends, as well as days of the week where service is available.
* routes.txt - **Required** - Transit routes. A route is a group of trips that are displayed to riders as a single service.
* stop_times.txt - **Required** - Times that a vehicle arrives at and departs from individual stops for each trip.
* stops.txt - **Required** - Individual locations where vehicles pick up or drop off passengers.
* trips.txt - **Required** - Trips for each route. A trip is a sequence of two or more stops that occurs at specific time.
* feed_info.txt - *Optional* - Additional information about the feed itself, including publisher, version, and expiration information.
* frequencies.txt - *Optional* - Headway (time between trips) for routes with variable frequency of service.
* shapes.txt - *Optional* - Rules for drawing lines on a map to represent a transit organization's routes.
* transfers.txt - *Optional* - Rules for making connections at transfer points between routes.

For more information about the files, you can visit: [General Transit Feed Specification Reference](http://developers.google.com/transit/gtfs/reference)