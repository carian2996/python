# python3

# Ian Castillo Rosales
# 05/26/2016

# Given a set of items and total capacity of a knapsack, find 
# the maximal value of fractions of items that fit into the knapsack.

# Task: The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input: The first line of the input contains the number n of items and the capacity W of a knapsack. 
# 	The next n lines define the values and weights of the items. The i-th line contain integers vi and wi 
# 	— the value and the weight of i-th item, respectively.
# Constraints: 1 ≤ n ≤ 103, 0 ≤ W ≤ 2*(10^6); 0 ≤ v_i ≤ 2*(10^6), 0 < w_i ≤ 2*(10^6) for all 1 ≤ i ≤ n. 
#	All the numbers are integers.
# Output: Output the maximal value of fractions of items that fit into the knapsack. The absolute value 
# 	of the difference between the answer of your program and the optimal value should be at most 10^(−3). 
# 	To ensure this, output your answer with at least four digits after the decimal point 
# 	(otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

# Time Limits: 5 sec.
# Memory Limit: 512Mb.

import sys
# from time import sleep

def get_optimal_value(capacity, weights, values):

	value = 0. # float type
	value_per_unit = [x/y for x, y in zip(values, weights)]
	# zip(): Make an iterator that aggregates elements from each of the iterables
	# Example:
	# x = [1, 2, 3] and y = [4, 5, 6]
	# zipped = zip(x, y)
	#
	# list(zipped)
	# [(1, 4), (2, 5), (3, 6)]


	for i in range(0, n):

		# print('i:', i)
		# print('value:', value)
		# print('capacity:', capacity)
		# print('weights:', weights)
		# print('values:', values)
		# print('value_per_unit:', value_per_unit, '\n')

		if capacity == 0: 
			return value
		
		index_max = value_per_unit.index(max(value_per_unit))

		if weights[index_max] > 0:
			piece = min(weights[index_max], capacity)
			
			value += piece*value_per_unit[index_max]
			
			if piece == weights[index_max]: value_per_unit[index_max] = 0
			weights[index_max] -= piece
			capacity -= piece

		# sleep(2)

	return value


if __name__ == "__main__":

	data = list(map(int, sys.stdin.read().split()))

	n, capacity = data[0:2]

	values = data[2:(2 * n + 2):2] # data[start:end:step]
	weights = data[3:(2 * n + 2):2]

	opt_value = get_optimal_value(capacity, weights, values)

	print("{:.4f}".format(opt_value))
