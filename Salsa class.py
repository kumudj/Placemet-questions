'''
Salsa class

Problem statement

A combined Salsa Lesson is to be conducted for two different classes having 8 students each, in a school. There are two queues of students, queue A, and queue B. You are given a string input 'A' denoting the queue sequence of students in queue A and a string input 'B' denoting the queue sequence of students in queue B.

A good pair is a pair containing one boy and one girl. Pairing the students at the Nth position of queue A with the students at the Nth position of queue B is the only possible method of pairing.

Write a program to help the organizer count the total number of good pairs that will be formed when the students are paired according to the method given above.

Your task is to return the percentage of good pairs among the total number of pairs that will be formed.

Note

1. A boy is denoted by the number 0 and a girl is denoted by number 1 in the string sequences.

2. If the answer is in float data type, it should be converted to int data type before returning.

Example - If the answer is 8.66, 8 should be returned.

Example 1

Input

00111101

10000001

Output

62

Explanation

62% pairs are good pairs among all the pairs

Example 2

Input

00110100

00000111

Output

50

Explanation

50% pairs are good pairs among all the pairs
'''

import math
def fun(a,b):
    count=0
    for i in range(8):
        res=int(a[i]) ^ int(b[i])
        if res==1:
            count=count+1
    temp=(count*100)/8
    result=int(math.floor(temp))
    return result

a=input()
b=input()
print(fun(a,b))