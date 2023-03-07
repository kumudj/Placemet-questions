'''
Lowest Common Multiple (LCM)

You are given an array of positive integers, arr, of size array_length. You are asked to build set S which consists of the LCM of every pair of adjacent elements in arr. Your task is to find the largest element in set S.

For example, for the array {1, 2, 3, 4}, set S = { lcm(1,2), lcm(2,3), lcm(3,4) } = {2, 6, 12}. The largest element is 12.

Notes

The array contains only positive integers.

Adjacent elements may NOT be circular, i.e. they may not wrap around the end of the array

Definition of LCM

A multiple of a number, num, is a number that can be divided by num. For example, the multiples of 5 are 5, 10, 15, 20, 25, and so on. The lowest common multiple (LCM) of two numbers, a and b, is the smallest positive number that is a multiple of both a and b.

Example 1

Input

4

1 3 2 4

Output 

6

Explanation

set S = {lcm(1, 3), lcm(3, 2), lcm(2, 4) } = {3, 6, 4}

Largest element = 6

Example 2

Input

5

7 3 2 9 12

Output

36

Explanation

set S = { lcm(7, 3), lcm(3, 2), lcm(2, 9), lcm(9, 12) } = {21, 6, 18, 36}

Largest element = 36

Input format
The first line of input denotes the size of an array.

The next lines contain the space-separated integers denoting the value of the array.

Output format
The output contains an integer denoting the largest element in set S as specified in the problem statement.

'''

import math
n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(1,n):
    ele=(arr[i-1]*arr[i])/math.gcd(arr[i-1],arr[i])
    ans.append(ele)
print(str(int(max(ans))))