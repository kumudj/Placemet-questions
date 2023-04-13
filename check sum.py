'''

Given an N (1 <= N <= 100), and array elements, write a program to find whether the sum of the elements are zero or not. If it is zero, print "Yes" else "No".



Example:

Input:

5

1 -1 2 -2 0

Output:

Yes

'''

n=int(input())
arr=list(map(int,input().split()))
if sum(arr)==0: print('Yes')
else: print('No')