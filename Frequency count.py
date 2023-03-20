'''

Frequency count

Problem Description

Given a string, find the frequencies of each of the characters in it. The input string contains only lowercase letters. The output string should contain a letter followed by its frequency, in the alphabetical order (from a to z).

Example

Input

babdc

Output

a1b2c1d1

Explanation

In the input string 'a' appears once, 'b' appears twice, 'c' and 'd' appear once. Therefore, in alphabetical order the output should be: a1b2c1d1



Input format
Input1: the input string





Output format
Return a string representing the frequency counts of characters in the input string.

'''

Max=26
def compress(s,n):
    freq=[0]*Max
    for i in range(n):
        freq[ord(s[i])-ord('a')] +=1
    for i in range(Max):
        if freq[i]==0:
            continue
        print("%c%d" %((chr)(i+ord('a')),freq[i]),end='')
str=input()
n=len(str)
compress(str,n)