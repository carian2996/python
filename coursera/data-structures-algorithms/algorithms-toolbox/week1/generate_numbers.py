# python3

from random import randint
from random import seed

# print("How many elements do you want to generate?")
n = int(input())
assert(n >= 2), "You should generate at least 2 elements"

# print("Choose the lowest value in the range of the array: ")
v_min = int(input())
assert(v_min >= 0), "You can't use negative numbers"

# print("Choose the highest value in the range of the array: ")
v_max = int(input())
assert(v_max <= 100000), "The numbers can't be greater than 100000"

v = [randint(v_min, v_max) for p in range(0, n)]

print(n)
print(*v)
