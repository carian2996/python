# Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of 
# the messages. You can pull the hour out from the 'From ' 
# line by finding the time and then splitting the string a 
# second time using a colon.

	# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print 
# out the counts, sorted by hour as shown below.

name = raw_input("Nombre del archivo: ")

try:
	handle = open(name)
except:
	print "El archivo no pudo ser abierto"

hours = []

for line in handle:
	line = line.rstrip()
	if not line.startswith("From "): continue
	line = line.split()
	time = line[5]
	time = time.split(':')
	hours.append(time[0])

distribution = dict()
for h in hours:
	distribution[h] = distribution.get(h, 0) + 1

sort_dist = sorted( [ (h, n) for (h, n) in distribution.items() ] )
for h, n in sort_dist:
	print h, n