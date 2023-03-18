'''
Problem statement

SecretMessage agency provides message encoding and decoding services for secure data transfer. The first step in decoding includes the removal of special characters from the message, as special characters and whitespaces do not hold any meaning.

Write an algorithm to help the agency find the number of special characters in a given message.

Example 

Input

gasg!g54@#vscsdls*

Output

4

Explanation

The special characters having no meaning are ['@', '#', '!', '*'].

Input format
The input consists of a string message, representing the message that needs to be decoded by the agency.

Output format
Print an integer representing the number of special characters present in a given message.

'''

string = input()
str = list(string)
count = 0
for i in range(len(str)):
    if str[i].isalnum():
        count = count + 1
print(len(str) - count)