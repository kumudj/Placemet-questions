'''
String permutations

Problem statement

You are given two strings 'X' and 'Y', each containing at most 1000 characters.

Write a program that can determine whether the characters in the first string 'X' can be rearranged to form the second string 'Y'. The output should be "yes" if this is possible and "no" if not.

Example 1

Input

input1: zbk

input2: zkb

Output

yes

Explanation

You can rearrange zbk to be zkb (by switching the k and the b). Hence the output is "yes".

Example 2

Input

input1: Mettl

input2: coding

Output

no

Explanation

As "Mettl" cannot be formed from rearranging "Coding". Hence the output is "no".

Input format
input1: the string 'X'

input2: the string 'Y'

Output format
Return "yes" or "no" accordingly

'''

a=list(input())
b=list(input())
a.sort()
b.sort()
if(a==b):
    print('yes')
else:
    print('no')