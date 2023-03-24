'''

Placement Season Begins

Problem Statement

The placement season has begun in a college. There are N number of students standing outside an interview room in a line. It is given that a person who goes in first has higher chances of getting selected. Each student has a number associated with them known as the problem-solving capability (PSC). The higher the capability, the higher the chances of selection. Now, each student wants to know the number of students ahead of him/her who have more problem-solving capability than him/her. Find this number for each student.

Example 1

Input

6

4 9 5 3 2 10

Output

0 0 1 3 4 0

Explanation

The first student has no one ahead of him/her. So, the answer is 0.

The second student has PSC greater than the first. So, the answer is 0.

Third student 9 is greater than 5. So, the answer is 1

Fourth student 9, 4 and 5 are greater than 3. So, the answer is 3.

Fifth student 3, 5, 9 and 4 are greater than 2. So, the answer is 4.

Sixth student No one ahead has a greater PSC. So, the answer is 0

Example2

Input

5

3 4 1 5 2

Output

0 0 2 0 3

Explanation

The first student has no one ahead of him/her. So, the answer is 0.

The second student has PSC greater than the first. So, the answer is 0.

Third student 3 and 4 are greater 1. So, the answer is 2

Fourth student No number ahead is greater than 5. So, the answer is 0.

Fifth student 3, 4 and 5 are greater than 2. So, the answer is 3.

Input format
input1: An integer N, which denotes the number of students present.

input2: An array of size N, denoting the problem-solving capability of the students.

Output format
An array of size N denoting the required answer for each student.

'''


n=int(input())
arr=list(map(int,input().split()))
print(0,end=' ')
for i in range(1,n):
    count=0
    for j in range(0,i):
        if arr[j] >= arr[i]:
            count=count+1
    print(count,end=' ')