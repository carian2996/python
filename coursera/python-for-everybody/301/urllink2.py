# Ian Castillo Rosales
# 09/11/2015

import urllib
from BeautifulSoup import *

url = raw_input('Enter: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')
numbers = []
for tag in tags:
    # Look at the content of a tag and convert into integer
    number = int(tag.contents[0])
    # Append into the numbers list
    numbers.append(number)

# Print the sum of the numbers
print sum(numbers)

