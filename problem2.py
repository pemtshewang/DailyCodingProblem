'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at

index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 

If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

from typing import List #recommended because it follows static typing protocol for time complexity
def solve(arr)->List[int]:
    ans=list()
    for i,val_i in enumerate(arr):
        curr_product = 1
        for j,val_j in enumerate(arr):
            if i!=j:
                curr_product *= val_j
        ans.append(curr_product)
    return ans          

print(solve(list(map(int,input().split()))))


