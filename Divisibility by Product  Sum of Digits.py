'''
Divisibility by Product / Sum of Digits

Problem statement

You are given an array of positive integers, arr, of size array_length. How many elements in arr are perfectly divisible by either the product or the sum of their digits?

Example 1

Input

1

303

Output

0

Explanation

Sum of digits of 303 = 6, the product of digits of 303 = 9

303 is not divisible by 6 or 9, hence the output is 0.

Example 2

Input

2

14

7

Output

1

Explanation

arr contains two elements, 14 and 7

Sum of digits of 14 = 5, product of digits of 14 = 4

14 is not divisible by 5 or 4.

Sum of digits of 7 = 7. Product of digits of 7 = 7

7 is divisible by 7

Therefore, the output is 1.

Example 3

Input

3

25

36

45

Output

2

Explanation

arr contains three elements, 25, 36, and 45

Sum of digits of 25 = 7, the product of digits of 25 = 10

25 is not divisible by 7 or 10

Sum of digits of 36 = 9, the product of digits of 36 = 18

36 is divisible by both 9 and 18

Sum of digits of 45 = 9, the product of digits of 45 = 20

45 is divisible by 9.

Therefore, the output is 2.

Input format
The first line contains an integer, array_length, denoting the number of elements in arr.

Each line i of the arry_length subsequent lines(where 0 <= i < array_length) contains an integer describing arr[i].

Output format
The output prints an integer denoting the number of elements in arr that are perfectly divisible by either the product or sum of their digits as specified in the problem statement.

'''

def divisible(arr,n):
    count=0
    for i in range(n):
        sum=0
        product=1
        temp=arr[i]
        while(temp!=0):
            rem=temp%10
            sum=sum+rem
            if(rem!=0):
                product=product*rem
            temp=temp//10
        if arr[i]%sum==0 or arr[i]%product==0:
            count=count+1
    return count
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(divisible(arr,n))