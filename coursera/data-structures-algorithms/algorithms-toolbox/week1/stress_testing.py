from random import randint
from random import seed

def MaxPairwiseProduct(n, v):
	assert(len(v) == n) 						# Is the length of the vector equal to n?

	result = 0

	for i in range(0, n):
	    for j in range(i+1, n):
	        if v[i]*v[j] > result:
	            result = v[i]*v[j]
	
	return result


def MaxPairwiseProductFast(n, v):
	assert(len(v) == n)
	
	max1_i = -1
	for i in range(0, n):
  		if max1_i == -1 or v[i] > v[max1_i]:
  			max1_i = i

	max2_j = -1
	for j in range(0, n):
  		if j != max1_i and (max2_j == -1 or v[j] > v[max2_j]):
  			max2_j = j

	return v[max1_i] * v[max2_j]


print("Choose a range to generate the length of the array: ")
n_min = int(input())
n_max = int(input())

print("Choose a range to generate the elements of the array: ")
v_min = int(input())
v_max = int(input())

print("Choose an integer for the seed: ")
s = int(input())

seed(s)

while True:

	n = randint(n_min, n_max)
	print(n)

	v = [randint(v_min, v_max) for p in range(0, n)]
	print(*v)

	res1 = MaxPairwiseProduct(n, v)
	res2 = MaxPairwiseProductFast(n, v)

	if res1 != res2:
		print("Wrong answer:", res1, res2)
		break
	else:
		print("OK")