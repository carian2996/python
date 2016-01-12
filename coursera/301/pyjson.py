# Ian Castillo Rosales
# 07 / 12 / 2015
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum

import json
import urllib
from BeautifulSoup import *

url = raw_input("Enter a valid URL: ")
data = urllib.urlopen(url).read()

print 'Retrieved', url
print 'Retrieved', len(data), 'characters'

info = json.loads(data)
print 'Count:', len(info['comments'])
comments = info['comments']

total_count = 0
for item in comments:
    total_count += int(item['count'])
print 'Sum:', total_count

