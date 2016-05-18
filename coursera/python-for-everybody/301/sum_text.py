# Ian Castillo Rosales
# 27 / 10 / 2015
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in
# the file and compute the sum of the numbers.

import re

with open("regex_sum_actual.txt") as text:
    content = text.read()

numbers = re.findall("[0-9]+", content)
numbers = map(int, numbers)

print sum(numbers)