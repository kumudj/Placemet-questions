'''

You are required to implement the following function

int MaxExponents (int a, int b); 

You have to find and return the number between ‘a’ and ‘b’ ( range inclusive on both ends) which has the maximum exponent of 2. 

The algorithm to find the number with a maximum exponent of 2 between the given range is 

Loop between ‘a’ and ‘b’. Let the looping variable be ‘i’. 
Find the exponent (power) of 2 for each ‘i’ and store the number with a maximum exponent of 2 so far in a variable, let say ‘max’. Set ‘max’ to ‘i’ only if ‘i’ has more exponent of 2 than ‘max’. 
Return ‘max’. 
Assumption

a <b 

Note

If two or more numbers in the range have the same exponents of 2, return the small number. 

Example 

Input

7 

12 

Output

8 

Explanation

Exponents of 2 in: 

7-0 

8-3 

9-0 

10-1 

11-0 

12-2 

Hence maximum exponent if two is 8.

Input format
Integer values of a and b.

Output format
Maximum exponent value.

'''

def count_exp(i):
    count=0
    while i%2==0 and i!=0:
        count+=1
        i=i//2
    return count
def max_exp(a,b):
    max,num=0,a
    for i in range(a,b+1):
        temp=count_exp(i)
        if temp>max:
            max,num=temp,i
    return num
a,b=map(int,input().split())
print(max_exp(a,b))