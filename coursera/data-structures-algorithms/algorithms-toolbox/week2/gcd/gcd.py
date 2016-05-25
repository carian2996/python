# python3
import sys

def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def fast_gcd(a, b):
	if b == 0: return a
	rem_a = a % b

	return fast_gcd(b, rem_a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    assert(1 <= a and 1 <= b), "The number should be greater than 1"
    assert(a <= 2000000000 and b <= 2000000000), "The number should be less than 2x10^9"

    print(fast_gcd(a, b))
    # print(gcd(a, b))
