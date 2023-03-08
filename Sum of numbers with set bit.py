'''
Sum of numbers with set bit

You are given a function,

int SumofSetBitNumbers(int n, int set);

The function accepts two integers ‘n’ and ‘set’ as its argument where ‘n’ is the number of bits and ‘set’ is the number of set bits. Implement the function to find the sum of all numbers possible from ‘n’ bits having the count of ‘set’ bits equal to set.

Note

n > 0

set >= 0

Example

Input

n: 3

set: 2

Output

14

Explanation

All possible 3 bit numbers are 0, 1, 2, 3, 4, 5, 6, 7 with binary representation 000, 001, 010, 011, 100, 101, 110, 111. Numbers with 2 bits set are 3, 5 and 6 summation of which is equal to 14.

'''

def fun(n,set):
    list=[]
    sum=0
    for i in range(2**n):
        list.append(bin(i).replace('0b',''))
    for i in range(len(list)):
        if list[i].count('1')==set:
            sum=sum+int(list[i],2)
    return sum
n=int(input())
set=int(input())
print(fun(n,set))