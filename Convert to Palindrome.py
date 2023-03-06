'''
Convert to Palindrome

Problem statement

A palindrome is a sequence of characters that has the property of reading the same in either direction. You are given a function.

Char* Convertpalindrome ( char* str );

The function accepts a string ‘str’ .Implement the function to find and return the minimum characters required to append at the end of string ‘str’ to make it palindrome.

Assumption

String will contain only lower case English alphabets.

Length of string is greater than equal to 1.

Note

If string is already palindrome then return “NULL”.

You have to find the minimum characters required to append at the end of string to make it palindrome.

Example1

Input

abcdc

Output

ba

Explanation

If we append 'ba' at the end of the string 'abcdc', it becomes 'abcdcba' (i.e. A palindrome string).

Example2

Input

abcde

Output

dcba

Explanation

If we append 'dcba' at the end of the string 'abcde', it becomes 'abcdedcba' (i.e. A palindrome string).

Input format
Input is a single string.

Output format
Output contains the characters to make the input string a palindrome.

'''

def ctp(l):
    le=len(l)
    for i in range(le):
        le=len(l)
        if l[i] != l[le-i-1]:
            l.insert(le-i,l[i])
        else:
            break
        s=''.join(l)
        if s==s[::-1]:
            s=s.replace(s1,'')
    print(s)
s1=input().strip()
l=list(s1)
ctp(l)
