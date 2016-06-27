# python3

# Ian Castillo Rosales
# 06/27/2016

# The edit distance between two strings is the minimum number of insertions, deletions, and mismatches 
# in an alignment of two strings.

# Task: The goal of this problem is to implement the algorithm for computing the edit distance between two strings.
# Input: Each of the two lines of the input contains a string consisting of lower case Latin letters.
# Constraints: The length of both strings is at least 1 and at most 100.
# Output: Output the edit distance between the given two strings.

# Time Limits: 10 sec.
# Memory Limit: 512Mb.

from numpy import zeros

def edit_distance(x, y):
	D = zeros((len(x) + 1, len(y) + 1), int)
	
	D[0, 1:] = range(1, len(y) + 1)
	D[1:, 0] = range(1, len(x) + 1)

	for i in range(1, len(x) + 1):
		for j in range(1, len(y) + 1):
			delt = 1 if x[i-1] != y[j-1] else 0
			D[i, j] = min(D[i-1, j-1] + delt, D[i-1, j] + 1, D[i, j-1] + 1)
	return D[len(x), len(y)]

if __name__ == "__main__":
	print(edit_distance(input(), input()))
