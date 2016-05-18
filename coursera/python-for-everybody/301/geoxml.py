# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.

# Ian Castillo Rosales
# 25/11/2015

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url: ')

uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0

for count in counts:
    total += int(count.text)

print total