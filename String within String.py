'''

String within String

Problem Statement

Given two strings, 'X' and 'Y' (length(X) >= 1, length(Y) <= 10000), find out if 'Y' is contained in 'X'. Return "yes", if 'Y' is contained in 'X', "no", if not.

Example1

Input

abac

ab

Output

yes

Explanation

Since string given in input2 is a part of the string given in input1, hence, yes is returned.

Example2

Input

abab

baaa

Output

no

Explanation

Since string given in input2 is not a part of the string given in input1, hence, no is returned.

Input format
input1: the string 'X'

input2: the string 'Y'

Output format
Return "yes" if string "Y" is contained in string "X", else, return "no"


'''

a=input()
b=input()
if b in a:
    print('yes')
else:
    print('no')