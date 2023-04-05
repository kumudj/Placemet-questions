'''

You are required to implement the following function

int differenceofSum(int n, int m);

The function accepts two integers n, m as arguments Find the sum of all numbers in the range from 1 to m(both inclusive) that are not divisible by n. Return difference between the sum of integers not divisible by n with the sum of numbers divisible by n.

Assumption

n>0 and m>0 

Sum lies between integral range 

Example 

Input 

n:4 

m:20 

Output 

90 

Explanation 

Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60 

Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150 

Difference 150 – 60 = 90 

Input format
Two integer inputs are the values of n & m respectively.

Output format
Output is the result of integer type.

'''

n=int(input())
m=int(input())
a=0
b=0
for i in range(1,m+1):
    if i%n==0:
        a+=i
    else:
        b+=i
print(b-a)