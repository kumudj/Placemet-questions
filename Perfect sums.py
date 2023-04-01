'''

Perfect sums

Problem Statement

A perfect sum is the sum of two or more elements of an array which is equal to a given number. Your task is to write a function to compute the number of perfect sums existing in an array.

Note

If no such sum exists, return 999. Also, if the input array is not an integer array, then also return 999

Example1

Input

5

9 7 3 12 7

Output

14

Explanation

Here, the sum of elements 7 + 7 = 14. Hence, the number of perfect sums in the given array is 1. Therefore, 1 is returned as the output.

Example2

Input

5

4 7 8 2 3

Output

12

Explanation

Here, the sum of elements 8 + 4 = 12 and 7 + 3 + 2 = 12. Hence, the number of perfect sums in the given array is 2. Therefore, 2 is returned as the output.

Input format
input1: An integer value representing the length of the integer array

input2: An integer array of length N

input3: An integer value representing the number, the perfect sum must be equal to.

Output format
Return the number of perfect sums existing in the array.


'''

import itertools
def subsets(arr,n):
    return list(itertools.combinations(arr,n))

n=int(input())
arr=list(map(int,input().split()))
k=int(input())
res=[]
for i in range(n):
    res.append(subsets(arr,i+1))
add=[]
for i in range(len(res)):
    for j in range(len(res[i])):
        add.append(sum(res[i][j]))
count=0
for i in add:
    if i==k:
        count+=1
print(count)