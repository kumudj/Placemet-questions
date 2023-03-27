'''

Wedding Game

Problem Statement

In a wedding that you are attending, there are some chairs that have digits inscribed at their backs. The chairs are lined in a row such that they form a string of the digits. Find the minimum number of sets M that can be formed from these digits such that:

1. The number of digits in each set is one or more than one.

2. Each set is formed using consecutive digits and no digit can be used more than once.

3. In each set, the number formed using the digits is less than or equal to Y.

Example1

Input

1234

4

4

Output

4

Explanation

Only 4 sets are possible that form a number less than or equal to 4, i.e. {1}, {2}, {3} and {4}.

Example2

Input

1234

30

4

Output

3

Explanation

Only 3 sets are possible that form a number less than or equal to 30, i.e. {12}, {3}, {4} or {1}, {23}, {4}.

Input format
input1: S, string of digits

input2: Y, No number should be greater than Y

input3: Size of the String S

Output format
Your function should return M, the minimum number of sets

'''


def minset(s,x):
    count=0
    n=0
    l=len(s)
    f=False
    for i in range(l):
        n=n*10+int(s[i])
        if n<=x:
            f=True 
        else:
            if f:
                count+=1
                n=int(s[i])
                f=False
            if n<=x:
                f=True 
            else:
                n=0
    if f==True:
        count+=1
    return(count)
s=input()
x=int(input())
n=int(input())
print(minset(s,x))