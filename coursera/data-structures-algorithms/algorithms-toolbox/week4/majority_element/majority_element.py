# python3

# Ian Castillo Rosales
# 06/22/2016

import sys

def majority_element(v, left, right):
    if left == right: return -1             # Empty array
    if left + 1 == right: return v[left]    # One element array    
    
    m = (left + right - 1) // 2             # Find the middle point

    left_v = majority_element(v, left, m)
    right_v = majority_element(v, m + 1, right)

    lv_count = 0
    for i in range(left, right):
        if v[i] == left_v:
            lv_count += 1
    if lv_count > (right - left) // 2:
        return left_v

    rv_count = 0
    for j in range(left, right):
        if v[j] == right_v:
            rv_count += 1
    if rv_count > (right - left) // 2:
        return right_v

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *v = list(map(int, input.split()))

    if majority_element(v, 0, n) != -1: 
        print(1)
    else:
        print(0)
