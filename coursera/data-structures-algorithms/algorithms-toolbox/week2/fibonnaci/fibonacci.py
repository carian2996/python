# python3

# Ian Castillo Rosales
# 05/26/2016

# Problem Introduction: The Fibonacci numbers are defined as follows: 
#	F0 = 0, F1 = 1, and Fi = Fi−1 + Fi−2 for i ≥ 2.

# Task: Given an integer n, find the nth Fibonacci number Fn. 
# Input: The input consists of a single integer n. 
# Constraints: 0 ≤ n ≤ 45.
# Output: Fn.

# Time Limits: 5 sec.
# Memory Limit: 512Mb.

def fibonacci(n):
	assert(0 <= n <= 45), "n should be between 0 and 45"

	F = []
	F.append(0)
	F.append(1)

	for i in range(2, n + 1):
		F.append(F[i - 1] + F[i - 2])

	return F[n]

if __name__ == "__main__":
	n = int(input())
	print(fibonacci(n))
