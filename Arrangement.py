'''

Arrangement

Problem Statement

Given an array of size n, write a function to rearrange the numbers of the array in such a way that even and odd numbers are  arranged alternatively in increasing order.

Example1

Input

5

9 12 23 8 5

Output

5 8 9 12 23

Explanation

As the numbers are to be arranged in increasing order hence we start with 5 in the given array, also the starting number is odd therefore the next number has to be even and has to be smallest in even number i.e., 8… & so on. Hence the output is {5, 8, 9, 12, 23}

Example2

Input

5

47 49 36 98 90

Output

36 47 90 49 98

Explanation

In the given array, 36 is the smallest number hence we start with it and arrange the series as even-odd alternatively.

Input format
input1: Array size i.e. n

input2: Array elements (separated by comma)



Output format
Return the updated array

'''

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
od=[]
ev=[]
for i in range(n):
    if arr[i]%2==0:
        ev.append(arr[i])
    else:
        od.append(arr[i])
k=min(len(od),len(ev))
for i in range(k):
    if min(arr)%2==0:
        print(ev[i],end=' ')
        print(od[i],end=' ')
    else:
        print(od[i],end=' ')
        print(ev[i],end=' ')
if len(od)>len(ev):
    print(*od[k:],end=' ')
if len(ev)>len(od):
    print(*ev[k:],end=' ')