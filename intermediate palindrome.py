'''

Problem statement

Write a program such that it takes a lower limit and upper limit as inputs and prints all the intermediate palindrome numbers excluding the boundaries. 

Example

Input

10 80 

Output

11 22 33 44 55 66 77

Input format
The two integer inputs are the values of upper and lower limits respectively.

Output format
Output integer line is the palindrome numbers in the range.

'''

a=int(input())
b=int(input())
for i in range(a+1,b):
    l=[str(it) for it in str(i)]
    if l==l[::-1]:
        print("".join(l), end=' ')

    