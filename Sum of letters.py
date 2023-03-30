'''

Sum of letters

Problem Statement

During a class assessment, a teacher asks students to solve the following problem:

If A = 0, B = 1, C = B + A, D = C + B, and so on, find the sum of the alphabets of a given word.

Example 1

Input

MAN

Output

377

Explanation

Given the above scenario, the values of M, A, and N are 144, 0, and 233 respectively. Hence, the sum returned is 144 + 0 + 233 = 377,

Example 2

Input

MORE

Output

2121

Explanation

Given the above scenario, the values of M, O, R and E are 144, 377, 1597, and 3 respectively. Hence, the sum returned is 144 + 377 + 1597 + 3 = 2121.



Input format
input1: String representing any word

Output format
Return an integer value that represents the sum of all the alphabets in input1, as per the above-given scenario.
'''

word = input()
word = [char for char in word]
fib = []
sum = 0
fib.append(0)
fib.append(1)
for i in range(2, 27):
    fib.append(fib[i - 1] + fib[i - 2])
alpha = []
for i in range(1, 27):
    alpha.append(chr(i + 64))
for i in range(len(word)):
    index = alpha.index(word[i])
    sum = sum + fib[index]
print(sum)
