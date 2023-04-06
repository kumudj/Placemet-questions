'''

Problem Statement 

A carry is a digit that is transferred to the left if the sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time 

You are required to implement the following function 

int NumberOfCarries(int num1, int num2); 

The functions accept two numbers ‘num1’ and ‘num2’ as their arguments. You are required to calculate and return the total number of carriers generated while adding digits of two numbers ‘num1’ and ‘ num2’. 

Assumption

num1, num2 >= 0 

Example

Input 

451 

349 

Output 

2 

Explanation: 

Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned. 

Input format
Input integers are the values of num1 & num2 respectively.

Output format
Output integer is the number of carrying operations.

'''

a=input()
b=input()
l=max(len(a),len(b))
a='0'*(l-len(a))+a
b='0'*(l-len(b))+b

c=0
k=0
for i in range(l):
    m=int(a[l-i-1])
    n=int(b[l-i-1])
    if m+n+c>9:
        c=(m+n+c)//10
        k+=c
    else:
        c=0
    
print(k)    