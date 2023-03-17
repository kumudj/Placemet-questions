'''

The Cuckoo Sequence

Problem Statement

A Cuckoo Sequence is defined as shown.

Cuckoo[1] = 0

Cuckoo[2] = 1

Cuckoo[n] = 1*Cuckoo[n-1] + 2*Cuckoo[n-2] + 3*1, for n > 2

Given n(1 <= n <= 109), find Cuckoo[n].

Example1

Input

3

Output

4

Explanation

Cuckoo[n] = 1*Cuckoo[n-1] + 2*Cuckoo[n-2] + 3*1

Cuckoo[3] = 1*Cuckoo[1] + 3*1

Cuckoo[3] = 1*1 + 2*0 + 3*1

Cuckoo[3] = 4

Example2

Input

2

Output

1

Explanation

Cuckoo[2] = 1 as given in the question.

Input format
Input1: Integer ‘n’

Output format
Return the value of Cuckoo[n].

'''

def cuckoo(n):
    if n == 1 or n == 2:
        return n-1
    else:
        return 1*cuckoo(n-1)+2*cuckoo(n-2)+3*1
n = int(input())
print(cuckoo(n))
