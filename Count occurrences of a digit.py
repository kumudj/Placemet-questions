'''
Count occurrences of a digit

Problem statement

Implement the following function:

int CountDigiOoccurrences(int l, int u, int x);

The function accepts 3 positive integers ‘l’, 'u' and 'x' as its arguments. You are required to calculate the number of occurrences of a digit 'x' in the digits of numbers lying in the range between ‘I’ and 'u' both inclusive, and return the same.

Note

I < u

0 < x < 9

Example

Input

I: 2

u: 13

x: 3

Output

2

Explanation

The number of occurrences of digit 3 in the digits of numbers lying in the range [2, 13] both inclusive is 2, ie (3, 13), hence 2 is returned.

Input format
The input accepts the three integers separated by a new line as given in the question.

Output format
The output is a single integer type.

'''

def fun(l,u,x):
    count=0
    for i in range(l,u+1):
        temp=i
        while temp!=0:
            rem=temp%10
            if rem==x:
                count=count+1
            temp=temp//10
    return count

l=int(input())
u=int(input())
x=int(input())
print(fun(l,u,x))