'''
String Reverse

﻿You are given a function,

char *ReverseString(char *s);

The function accepts a string ‘s’ that contains alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’) along with other characters. Reverse this string ‘s’ in such a way that only alphabets are reversed and other characters are not affected.

Note

Return null if it is null.

Null refers to None in the case of Python

Example

Input

a^bk$c

Output

c^kb$a

Explanation

Characters ‘^’ and ‘$’ are at their original positions while all alphabets got reversed.

Input format
Input is a single string.

Output format
Output is the reversed string with conditions satisfied.

'''

def reverse(text):
    index=[]
    a=[]
    for i in range(len(text)):
        if text[i].isalpha():
            a.append(text[i])
            index.append(i)
    a.reverse()
    for i in range(len(index)):
        text[index[i]]=a[i]
    return text
text=input()
res=reverse(list(text))
print(''.join(res))