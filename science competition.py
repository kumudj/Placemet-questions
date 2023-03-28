'''

Problem statement

A science competition was organized in a school, with N number of students taking part. Each student scored a certain number of points. Now, the school wishes to send a certain number of students (K) to the science competition at State Level. The students need to be selected in such a way that the sum of their total score is as high as possible.

Write an algorithm to identify the scores of the student who will take part in the science competition at the State Level.

Note

The sequence of the selected scores of the students should be the same as that of the actual scores(input).

Example

Input

5

89 14 5 10 50

2

Output

89 50

Explanation

As the count of students to be selected is 2 (k=2). We have to select the 2 scores whose sum will be the greatest. Score 89 & 50 are the two scores that will make the maximum sum (139).

So, the output is (89, 50).

Input format
The first line of the input consists of an integer - numStudents, representing the number of students in the science competition (N). 

The next line consists of N space-separated integers - studScore1, studScore2, .... studScoreN representing the scores for all the participants.

The next line consists of an integer - state-level count representing the count of students to be sent to the science competition at State Level (K).

Output format
Print K space-separated integers representing the scores of the students who are selected for the science competition at the State Level.

'''

import itertools
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
subset=list(itertools.combinations(arr,k))
add=[]
for i in range(len(subset)):
    temp=sum(subset[i])
    add.append(temp)
index=add.index(max(add))
tup=list(subset[index])
tup.sort(reverse=True)
print(*tup)
