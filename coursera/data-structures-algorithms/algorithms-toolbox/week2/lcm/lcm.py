# Uses python3
import sys

def gcd(a, b):
	if b == 0: return a
	rem_a = a % b

	return gcd(b, rem_a)

def lcm(a, b):
    return int((a*b)/gcd(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

