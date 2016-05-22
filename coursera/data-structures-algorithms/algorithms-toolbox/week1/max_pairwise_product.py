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

def MaxPairwiseProduct(n, a):
	assert(len(a) == n), "n should be equal to the length of the array"

	result = 0

	for i in range(0, n):
	    for j in range(i+1, n):
	        if a[i]*a[j] > result:
	            result = a[i]*a[j]
	
	print(result)


def MaxPairwiseProductFast(n, a):
	assert(len(a) == n), "n should be equal to the length of the array"
	
	max1_i = -1
	for i in range(0, n):
  		if max1_i == -1 or a[i] > a[max1_i]:
  			max1_i = i

	max2_j = -1
	for j in range(0, n):
  		if j != max1_i and (max2_j == -1 or a[j] > a[max2_j]):
  			max2_j = j

	print(a[max1_i] * a[max2_j])


# Maximum pairwise product
n = int(input())
a = [int(x) for x in input().split()]

# MaxPairwiseProduct(n, a)
MaxPairwiseProductFast(n, a)