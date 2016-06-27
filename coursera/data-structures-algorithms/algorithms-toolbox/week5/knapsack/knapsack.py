# python3

# Ian Castillo Rosales
# 06/27/2016

# This problem is about implementing an algorithm for the knapsack without repetitions problem.

# Task: In this problem, you are given a set of bars of gold and your goal is to take as much gold 
# 	as possible into your bag. There is just one copy of each bar and for each bar you can either 
# 	take it or not (hence you cannot take a fraction of a bar).
# Input: The first line of the input contains the capacity W of a knapsack and the number n of bars of gold. 
# 	The next line contains n integers w_0, w_1, ..., w_{n-1} defining the weights of the bars of gold.
# Constraints: 1 ≤ W ≤ 10^4; 1 ≤ n ≤ 300; 0 ≤ w_0, ..., w_{n-1} ≤ 105
# Output: Output the maximum weight of gold that fits into a knapsack of capacity W.

# Time Limits: 10 sec.
# Memory Limit: 512Mb.

import sys
from numpy import zeros

def optimal_weight(W, w):
	knapsack = zeros((len(w) + 1, W + 1), int)

	for i in range(1, len(w)+1):
		for j in range(1, W+1):
			knapsack[i, j] = knapsack[i-1, j]
			if w[i-1] <= j:
				val = knapsack[i-1, j - w[i-1]] + w[i-1]
				if knapsack[i, j] < val: knapsack[i, j] = val
	return knapsack[len(w), W]

if __name__ == '__main__':
	input = sys.stdin.read()
	W, n, *w = list(map(int, input.split()))
	print(optimal_weight(W, w))
