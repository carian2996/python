# python3
import sys
from time import sleep

def dinamic_solve(n):
    v = [0]*(n+1)
    v[1] = 1
    print(v)

    for i in range(1, n):
        print('i:', i)
        print('v[i]:', v[i])
        # sleep(5)

        if not v[i]: continue
        if v[i+1] == 0 or v[i+1] > v[i] + 1: v[i+1] = v[i] + 1

    print('')
    print('v:', v)
    solution = []
    while n > 1:
        solution.append(n)
        if v[n-1] == v[n] - 1: n = n-1
        if n%2 == 0 and v[n//2] == v[n] -1: n = n//2
    solution.append(1)
    return solution.reverse()

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

n = int(input())
print(dinamic_solve(n))
# sequence = dinamic_solve(n)
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
