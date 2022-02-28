'''Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
from typing import List

def solve(arr,k)->bool:
    for i,val_i in enumerate(arr):
        for j,val_j in enumerate(arr):
            if i != j:
                if val_i+val_j == k:
                    return True
    return False

arr:List[int] = list(map(int,input().split(' ')))
k:int = int(input())
print(solve(arr,k))
