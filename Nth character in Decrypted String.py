'''
Nth character in Decrypted String

Problem Statement

Every character in the input string is followed by its frequency. Write a function to decrypt the string and find the nth character of the decrypted string. If no character exists at that position then return “-1”. For eq:- if the input string is “a2b3” the decrypted string is “aabbb”

Note

The frequency of encrypted string cannot be greater than a single digit i.e., < 10.

Example1

Input

a1b1c3

5

Output

c

Explanation

The decrypted string is “abccc”, hence the 5th character in the decrypted string is “c”.

Example2

Input

a3b2

7

Output

-1

Explanation

The decrypted string is “aaabb”. Since the length of the decrypted string is less.
'''

def fun(str, n):
    encoded = ""
    occurence = 0
    i = 0
    while i < len(str):
        temp = ""
        occurence = 0
        while(i < len(str) and ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            temp += str[i]
            i += 1
        while(i < len(str) and ord(str[i]) >= ord('1') and ord(str[i]) <= ord('9')):
            occurence = occurence * 10 + ord(str[i]) - ord('0')
            i += 1
        for j in range(1, occurence + 1, 1):
            encoded += temp
    if occurence == 0:
        encoded += temp
    if len(encoded) < n:
        return -1
    else:
        return encoded[n - 1]

str = input()
n = int(input())
print(fun(str, n))