'''
Coding Marathon

Problem statement

N number of people participated in a coding marathon where they were asked to solve some problems. Each problem carried 1 mark and at the end of the marathon, the total marks that each person achieved was calculated.

As an organizer, you have the list of the total marks that each person achieved. You have to calculate the sum of the marks of top K scorers from the list.

Example 1

Input

input1: 4

input2: 2

input3: {4, 1, 2, 5}

Output

9

Explanation

Top 2 scores are 5 and 4. Sum = 5+4 = 9.

Example 2

Input

input1: 4

input2: 3

input3: {4, 3, 6, 1}

Output

13

Explanation 

Top 3 scores are 6, 4 and 3. Sum = 6+4+3 = 13.

Input format
input1: N, Total number of participants

input2: K, Top scorers

input3: An array of length N with the scores of all N participants

Output format
Return S, the sum of the marks of top K scorers from the list.

'''

a=int(input())
b=int(input())
arr=list(map(int,input().split()))
arr.sort()
arr.reverse()
sum=0
for i in range(b):
    sum+=arr[i]
print(sum)