'''
Lowest Common Multiple (LCM)

Problem statement

Find the LCM of two given integers. Fill in a function that takes as inputs two integers and return their LCM.

Example 1

Input

input1: 2

input2: 3

Output 

6

Explanation

The LCM of 2 and 3 is 6

Example 2

Input

input1: 5

input2: 65

Output

65

Explanation 

The LCM of 5 and 65 is 65.

Input format
input1: First integer

input2: Second integer

Output format
Return the LCM of input numbers

'''

import math 
def lcm(n1,n2):
    gcd=math.gcd(n1,n2)
    prod=n1*n2
    return prod//gcd
n1=int(input())
n2=int(input())
print(lcm(n1,n2))