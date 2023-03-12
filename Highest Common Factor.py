'''
Highest Common Factor

Problem statement

Find the HCF (Highest Common Factor) of n numbers given in an integer array. Fill in the function HCF() and return the HCF

Example 1

Input

input1: 3

input2: {2, 4, 8}

Output

2

Explanation

The common factor for 2, 4, 8 are 1 and 2. Hence the HCF (Highest Common Factor) is 2.

Example 2

Input

input1: 5

input2: {10, 15, 20, 35, 70}

Output

5

Explanation

The common factor for 10, 15, 20, 35, 70 are 1 and 5. Hence the HCF (Highest Common Factor) is 5.

Input format
input1: the size array

input2: an integer array

Output format
Return the HCF of given numbers

'''

import math
def hcf(n1,n2):
    return math.gcd(n1,n2)
n=int(input())
arr=list(map(int,input().split()))
gcd=hcf(arr[0],arr[1])
for i in range(2,n):
    gcd=hcf(gcd,arr[i])
print(gcd)