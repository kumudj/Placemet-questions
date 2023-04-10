'''
Arithmetic Progression

Problem statement

Given the second and the third terms of an AP (-10^6 <= a2, a3 <= 10^6), find the nth (1 <= n <= 1000) term of the sequence

Example 1

Input

input1: 1

input2: 2

input3: 4

Output

3

Explanation

a2 = 1, a3 = 2, n = 4 d = 1 an = a4 = 3 (d refers to the common difference between adjacent terms in an arithmetic progression)

Example 2

Input

input1: 5

input2: 8

input3: 4

Output

11

Explanation

a2 = 5, a3 = 8, n = 4 d = 3, an = a4 = 11 (d refers to the common difference between adjacent terms in an arithmetic progression)


Input format
input1: Second element of series (Integer)

input2: Third element of series (Integer)

input3: Total number of elements in the series (Integer)

Output format
Return the nth element of the series

'''

a2=int(input())
a3=int(input())
n=int(input())
d=a3-a2
a=a2-d
an=a+(n-1)*d
print(an)
