# python3

def fibonacci(n):
	if n <= 1:
		return n

	return fibonacci(n - 1) + fibonacci(n - 2)

def fast_fibonacci(n):
	assert(0 <= n <= 45), "n should be between 0 and 45"

	F = []
	F.append(0)
	F.append(1)

	for i in range(2, n + 1):
		F.append(F[i - 1] + F[i - 2])

	return F[n]


print("Enter the n-th Fibonacci number you wish to calculate: ")
n = int(input())
print(fast_fibonacci(n))
# print("Slow solution:", fibonacci(n))
