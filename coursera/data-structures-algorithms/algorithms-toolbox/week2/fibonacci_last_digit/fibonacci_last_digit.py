# python3

def get_fibonacci_last_digit(n):
    assert(0 <= n <= 10000000), "n should be between 0 and 45"

    F = []
    F.append(0)
    F.append(1)

    for i in range(2, n + 1):
    	F.append((F[i - 1] + F[i - 2]) % 10)

    return F[n]


if __name__ == "__main__":
	n = int(input())
	print(get_fibonacci_last_digit(n))

