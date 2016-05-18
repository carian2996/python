# python2

# This program takes two numbers as input, with the next constrains: 0 <= a, b <=1 9.
# Add them and print the result.

import sys

input = sys.stdin.read() 	# read a standard input object
numbers = input.split()

a = int(numbers[0])
b = int(numbers[1])

print(a + b)
