'''

You are required to implement the following function

int FindNumbersDivisible(int a, int b, int divi):

The function takes three positive integers a, b and divi as input. Implement the function to find and return the count of all those numbers between 'a' and b' (both inclusive) which are divisible by 'divi'.

Input format
The three input integers are the values of a, b and divi respectively.

Output format
The output integer is the count of numbers divisible by div from a to b.

'''

a=int(input())
b=int(input())
div=int(input())
count=0
for i in range(a,b+1):
    if i%div==0:
        count+=1
print(count)
    