'''

Problem statement

7 types of Indian currency notes are given, ie, Re. 1, Rs. 2. Rs. 5, Rs10, Rs 20, Rs 50 and Rs 100.

You are required to implement the following function

int MinNumberOfNotes (int n);

The function accepts an integer 'n' as its argument. Implement the function to find and return the minimum number of notes required to form the amount 'n'.

Assumption

n>=0

Note

Return 0,if n=0
multiple notes of the same type can be used
Input format
Input integer is the value of n.

Output format
Output integer is the number of notes required.

'''

n=int(input())
if n==0:
    print(0)
n1=n//100
n=n%100
n2=n//50
n=n%50
n3=n//20
n=n%20
n4=n//10
n=n%10
n5=n//5
n=n%5
n6=n//2
n=n%2
n7=n
print(n1+n2+n3+n4+n5+n6+n7)
