# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.

# Ian Castillo Rosales
# 18/11/2015

import urllib
from BeautifulSoup import *

url = raw_input('Enter url: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')

    if i != range(count)[-1]:
        print 'Retrieving: ' + tags[position - 1].get('href', None)
    else:
        print 'Last Url: ' + tags[position - 1].get('href', None)

    url = tags[position - 1].get('href', None)
