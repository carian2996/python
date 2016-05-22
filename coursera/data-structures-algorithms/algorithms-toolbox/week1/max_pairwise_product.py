# python3

# Given a sequence of non-negative integers a_0, ..., a_(n-1),
# find the maximum pairwise product, that is, the largest integer 
# that can be obtained by multiplying two different elements from 
# the sequence (or, more formally, max_(0 <= i != j<=n-1) a_i a_j). 
# Different elements here mean a_i and a_j with i different of j 
# (it can be the case that a_i = a_j).


# The next algorithm take the first number in the array and multiplies
# by the rest of the number. Compares with the variable 'result' and
# saves it if the multiplication is greater than 'result'.

def MaxPairwiseProduct(n, v):
	
	assert(len(v) == n) 						# Is the length of the vector equal to n?

	result = 0

	for i in range(0, n):
	    for j in range(i+1, n):
	        if v[i]*v[j] > result:
	            result = v[i]*v[j]
	
	print(result)


def MaxPairwiseProductFast(n, v):
	
	assert(len(v) == n)
	
	max1_i = -1
	for i in range(0, n):
  		if max1_i == -1 or v[i] > v[max1_i]:
  			max1_i = i

	max2_j = -1
	for j in range(0, n):
  		if v[j] != v[max1_i] and (max2_j == -1 or v[j] > v[max2_j]):
  			max2_j = j

	print(v[max1_i] * v[max2_j])


# Maximum pairwise product
n = int(input())
v = [int(x) for x in input().split()]

MaxPairwiseProduct(n, v)
MaxPairwiseProductFast(n, v)