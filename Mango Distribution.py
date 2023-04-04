'''

Mango Distribution

Problem Statement

Given a number of mangoes and number of persons. Find the number of ways to distribute identical mangoes among identical persons.

Example1

Input 

2

2

Output

3

Explanation

All possible distributions of 2 identical mangoes to 2 identical persons are (1, 1), (2, 0) and (0, 2). Hence the output is 3.

Example2

Input

1

12

Output

1

Explanation

All possible distributions of 1 identical mango to 12 identical persons are 12. Hence the output is 12.

Input format
input1: the number of mangoes

input2: the number of persons



Output format
Return the number of ways to distribute identical mangoes among identical persons.
'''

def binomial_coefficients(n, m):
    res = 1
    if m > n - m:
        m = n - m
    for i in range(m):
        res *= (n - i)
        res /= (i + 1)
    return res
    
def calc_ways(m, n):
    if m == 1:
        return n
    if m < n:
        return 0
    ways = binomial_coefficients(n + m - 1, n - 1)
    return int(ways)
    
m = int(input())
n = int(input())
print(calc_ways(m, n))
