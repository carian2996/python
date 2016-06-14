# python3

# Ian Castillo Rosales
# 06/14/2016

# Task: The goal is, given two sequences a_1, a_2, . . . , a_n and b_1, b_2, . . . , b_n, find a permutation 
#   c of the second sequence such that the dot product of a_1, a_2, ..., a_n and bc_1,bc_2, ..., bc_n is minimum.
# Input: The first line contains an integer n, the second one contains a sequence of integers a_1,a_2, ..., a_n, 
#   the third one contains a sequence of integers b_1,b_2, ..., b_n.
# Constraints: 1 ≤ n ≤ 10^3; −105 ≤ a_i, b_i ≤ 105 for all 1 ≤ i ≤ n.
# Output: Output the minimum possible dot product.

# Time Limits: 5 sec.
# Memory Limit: 512Mb.

import sys

def min_dot_product(a, b):

    a.sort()
    b.sort(reverse = True)
    
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
