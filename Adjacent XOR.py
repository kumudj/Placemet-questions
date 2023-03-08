'''
Adjacent XOR

Problem statement

You are given an integer input num.

Write a program to perform the following operations

1. Obtain Z by converting num to Binary form.

2. For each bit A in Z, apply bitwise XOR operation with the adjacent bit present on its right, starting from the Most Significant Bit (MSB), store the obtained value back in bit A. Let the new binary number obtained by performing these operations be Y.

3. Obtain X by converting Y to a Decimal form.

Your task is to return the value of x.

[NOTE - Apply bitwise XOR operation of the Least Significant Bit (LSB) with 1 in Z].

Example 1

Input 

013

Output

6

Explanation

6 was obtained as the result after applying all the operations on num = 013

Example 2

Input

649

Output

922

Explanation

922 was obtained as the result after applying all the operations on num = 649

Input format
The first line contains an integer, num.

Output format
The output denotes an integer value

'''

def fun(n):
    arr = [0] * n
    temp = [0] * n
    t = 0
    base = 1
    index = 0
    while(n != 0):
        arr[index] = n % 2
        n = int(n / 2)
        index = index + 1
    temp[0] = arr[0] ^ 1
    for i in range(1, index):
        temp[i] = arr[i] ^ arr[i-1]
        
    for i in range(0, index):
        t = t + (temp[i] * base)
        base = base * 2
        
    return t
    
n = int(input())
print(fun(n))