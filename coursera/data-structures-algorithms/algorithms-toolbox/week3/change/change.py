# python3

# Ian Castillo Rosales
# 06/02/2016

# Problem Introduction: In this problem, you will design an algorithm for changing money optimally.

# Task. The goal in this problem is to find the minimum number of coins needed to change the input 
# value (an integer) into coins with denominations 1, 5, and 10. 
# Input: The input consists of a single integer m.
# Constraints: 0 ≤ m ≤ 10^3.
# Output Format: Output the minimum number of coins with denominations 1, 5, 10 that changes m.

# Time Limits: 5 sec.
# Memory Limit: 512Mb.

import sys

def get_change(n):

	assert(0 <= n <= 1000), "m should be between 0 and 1000"
    
    ten = 0
    five = 0
    one = 0

    while n >= 10:
    	n -= 10
    	ten += 1

    while n >= 5:
    	n -= 5
    	five += 1

    while n >= 1:
    	n -= 1
    	one += 1

    return ten + five + one

if __name__ == '__main__':
    n = int(input())
    print(get_change(n))