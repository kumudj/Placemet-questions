'''
Fibonacci sequence - Integers in an Array

Problem statement

You are given an array of non-negative integers, arr, of size array_length. How many elements in arr are Fibonacci numbers?

Fibonacci numbers, denoted F(n), form a sequence known as the Fibonacci sequence, in which each number is the sum of the two preceding numbers starting with 0 and 1.

That is F(0) = 0, F(1) = 1 and F(n) = F(n-1) + F(n-2)

The first 10 terms of the Fibonacci sequence are listed below

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Example 1

Input

4

1

1

1

1

Output

4

Explanation

1 is a Fibonacci number and it is contained in arr four times. Hence the output is 4.

Example 2

Input

5

2 4 8 16 31

Output

2

Explanation

2 and 8 are the only Fibonacci numbers in arr. Hence, the output is 2

Example 3

Input

7

0

1

2

3

4

5

4

Output

5

Explanation

0, 1, 2, 3 and 5 are the only Fibonacci numbers in arr. Hence the output is 5.
'''

def check(ele):
    if ele==1:
        return 1
    if ele==0:
        return 1
    a=0
    b=1
    c=0
    while c<ele:
        c=a+b
        a=b
        b=c
        if c==ele:
            return 1
    return 0

n=int(input())
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)
count=0
for i in range(n):
    if check(arr[i]) == 1 :
        count+=1
print(count)