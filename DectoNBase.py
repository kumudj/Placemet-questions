'''

Problem statement

﻿N-base notation is a system for writing numbers that use only n different symbols, This symbols are the first n symbols from the given notation list(Including the symbol for o) Decimal to n base notation are (0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:A,11:B and so on up to 35:Z) 

You are required to implement the following function

char* DectoNBase(int n, int num);

The function accepts positive integer n and num Implement the function to calculate the n-base equivalent of num and return the same as a string 

Steps: 

Divide the decimal number by n, Treat the division as the integer division 
Write the remainder (in n-base notation) 
Divide the quotient again by n, Treat the division as integer division 
Repeat step 2 and 3 until the quotient is 0 
The n-base value is the sequence of the remainders from last to first 
Assumption

1 < n < = 36 

Example 

Input 

n: 12 

num: 718 

Output 

4BA 

Explanation 

num Divisor quotient remainder 

718 12 59 10(A) 

59 12 4 11(B) 

4 12 0 4(4) 

Input format
The first line of input contains an integer denoting the value of n.

The second line of input contains an integer denoting the value of num.

Output format
The output prints the N-base notation.

'''

n=int(input())
num=int(input())
rem=[]
qua=num//n
rem.append(num%n)
while qua!=0:
    rem.append(qua%n)
    qua=qua//n
rem=rem[::-1]
eq=''
for i in rem:
    if i>9:
        temp=i-9
        temp=64+temp
        eq+=chr(temp)
    else:
        eq+=str(i)
print(eq)
