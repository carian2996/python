# Uses python3
import sys

def gcd(a, b):
	if b == 0: return a
	rem_a = a % b

	return gcd(b, rem_a)

def lcm(a, b):
	assert(1 <= a and 1 <= b), "The number should be greater than 1"
	assert(a <= 2000000000 and b <= 2000000000), "The number should be less than 2x10^9"

	return int( (a*b)//gcd(a, b) )


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
