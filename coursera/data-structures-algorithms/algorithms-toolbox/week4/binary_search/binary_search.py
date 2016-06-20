# python3

# Ian Castillo Rosales
# 06/20/2016

# Implement the binary search algorithm that allows searching very efficiently (even huge) 
# lists provided that the list is sorted.

# Task: The goal in this code problem is to implement the binary search algorithm.
# Input: The first line of the input contains an integer n and a sequence a_0 < a_1 < ... < a_{n−1} of 
#   n pairwise distinct positive integers in increasing order. The next line contains an integer k and 
#   k positive integers b_0, b_1, ..., b_{k−1}.
# Constraints: 1 ≤ n, k ≤ 105; 1 ≤ a_i ≤ 10^9 for all 0 ≤ i < n; 1 ≤ b_j ≤ 10^9 for all 0 ≤ j < k;
# Output: For all i from 0 to k−1, output an index 0 ≤ j ≤ n−1 such that a_j = b_i or −1 if there is no such index.

# Time Limits: 10 sec.
# Memory Limit: 512Mb.

import sys

def binary_search(v, low, high, k):
    if high < low: return -1

    mid = low + (high - low) // 2

    if k == v[mid]:
        return mid
    elif k < v[mid]:
        return binary_search(v, low, mid - 1, k)
    else:
        return binary_search(v, mid + 1, high, k)

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    
    n = data[0]
    v = data[1 : n + 1]

    assert(n == len(v)), 'Error in sorted vector length'
    
    for k in data[n + 2:]:
        print(binary_search(v, 0, n - 1, k), end = ' ')