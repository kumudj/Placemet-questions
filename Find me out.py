'''

Find me out

Problem Statement

For a given number N (0 < N <= 100), little Johnny wants to find out the minimum positive integer X divisible by N, where the sum of digits of X is equal to N, and X is not equal to N.

Note

If such a number X does not exist, then output should be -1

Example1

Input

9

Output

18

Explanation

Starting from1, the minimum positive integer to be returned by the function is 18 which is divisible by the sum of the digits of 18 is equal to 9, and 18 is not equal to 9. Therefore 18 is returned as the output.

Example2

Input

10

Output

190

Explanation

Starting from 1, the minimum positive integer to be returned by the function is 190 which is divisible by 10, the sum of the digits of 190 is equal to 10, and 190 is not equal to 10. Therefore 190 is returned as the output.

Input format
input1: An integer N

Output format
Return the minimum positive integer X

'''

n=int(input())
i=n+1
m=1
while(m!=0):
    if i%n==0:
        s=[int(a) for a in str(i)]
        
        s=sum(s)
        if s==n:
           print(i)
           m=0
    i+=1
