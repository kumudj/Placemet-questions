'''
Anagrams

Problem statement

An anagram is a word, phrase, or name formed by rearranging the letters of another word, phrase, or name.

Write a function to check if two given strings are anagrams or not. Return “yes” if they are anagrams, otherwise return “no”.

Example 1

Input

input1: build

input2: dubli

Output

yes

Explanation

First string can be rearranged to form the second string. Hence they are anagram of each other.

Example 2

Input

input1: beast

input2: yeast

Output

no

Explanation

The first string contains the letter ‘b’ which is not present in the second string. Similarly, the second string contains the letter ‘y’ which is not present in the first string. Hence, the two strings are not anagram of each other.

'''

a=list(input())
b=list(input())
a.sort()
b.sort()
if(a==b):
    print("yes")
else:
    print("no")