'''
Playing with Numbers

Problem statement

Ryan is given an array of random integers of size n, a number d is provided to him along with this array. He needs to develop a logic such that it shifts the given array elements by d positions towards the left. Write a function for him and return the updated array.

Example 1

Input

input1: 7

input2: {1, 2, 3, 4, 5, 6, 7}

input3: 2

Output

{3, 4, 5, 6, 7, 1, 2}

Explanation

For the given d, i.e., 2 for the above case such element is shifted by 2 places to left, and the initial 2 elements are required to be shifted from behind, hence array is being rotated

Example 2

Input

input1: 9

input2: {1, 7, 8, 5, 4, 6, 0, 2, 3}

input3: 3

Output

{5, 4, 6, 0, 2, 3, 1, 7, 8}

Explanation

As the elements are shifted 3 positions to the left, therefore initial 3 elements after being shifted appear at the tail of the array and accordingly, other elements are shifted 3 positions towards left.

'''

import numpy as np
n=int(input())
temp=list(map(int,input().split()))
shift=int(input())
arr=np.array(temp)
res=np.roll(arr,-shift)
print(*res)