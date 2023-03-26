'''

Cut and Add

Problem Statement

Harry and Potter took a word string. Harry chose a number M (less than the length of the string) and Potter chose N (less than the length of the string). Harry will cut M alphabets from the end of the string and then add it to the beginning and will give it to Potter. 

Then, Potter will also cut N alphabets from the end of the string, add it to the beginning and then give to Harry. This process will continue till they get the original word string back. For a given string and given values of M and N, find the number of turns in which they will get the original word string back.

Example1

Input

AbcDef

1

2

Output

4

Explanation

turn1: fAbcDe

turn2: DefAbc

turn3: cDefAb

turn4: AbcDef

Example2

Input

abcabc

1

1

Output

3

Explanation

turn1: cabcab

turn2: bcabca

turn3: abcabc

Input format
input1: Original word string

input2: Value of M

input3: Value of N

Output format
The number of turns to get back the original word string

'''


w=input()
m=int(input())
n=int(input())
count=1
w2=w[-m:]+w[:len(w)-m]
while w != w2:
    if count % 2 != 0:
        w2 = w2[-n:]+w2[:len(w)-n]
    else:
        w2 = w2[-m:]+ w2[:len(w)-m]
    count= count+1
print(count)