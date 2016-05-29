# python3

# Ian Castillo Rosales
# 05/29/2016

from random import randint
from random import seed

def naive_lcm(a, b):
	assert(1 <= a and 1 <= b), "The number should be greater than 1"
	assert(a <= 2000000000 and b <= 2000000000), "The number should be less than 2x10^9"

	n = 2
	mul_a = [a]
	mul_b = [b]

	lcm = 0

	if a == b:
		return a
	else:
		while True:
			mul_a.append(a*n)
			mul_b.append(b*n)

			# print(*mul_a)
			# print(*mul_b, "\n")

			if len(list(set(mul_a) & set(mul_b))) != 0:
				lcm = list(set(mul_a) & set(mul_b))
				return lcm[0]
				break

			n += 1

def gcd(a, b):
	if b == 0: return a
	rem_a = a % b

	return gcd(b, rem_a)

def lcm(a, b):
	assert(1 <= a and 1 <= b), "The number should be greater than 1"
	assert(a <= 2000000000 and b <= 2000000000), "The number should be less than 2x10^9"

	return int((a*b)/gcd(a, b))

print("Choose a range to generate numbers. Min: ")
range_min = int(input())
print("Max: ")
range_max = int(input())

print("Choose an integer for the seed: ")
s = int(input())

print("")

seed(s)

while True:
	a = randint(range_min, range_max)
	b = randint(range_min, range_max)
	print(a, b)

	res1 = naive_lcm(a, b)
	res2 = lcm(a, b)

	if res1 != res2:
		print("Wrong answer:", res1, res2, "\n")
		break
	else:
		print("OK", res1, res2, "\n")