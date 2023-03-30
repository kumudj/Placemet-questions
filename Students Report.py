'''

Students Report

Problem Statement

Given a list of N students, every student is marked for M subjects. Each student is denoted by an index value. Their teacher Ms. Margaret must ignore the marks of any 1 subject for every student. For this, she decides to ignore the subject which has the lowest class average.

Your task is to help her find that subject, calculate the total marks of each student in all the other subjects and then finally return the array of the total marks scored by each student.

Example 1

Input

3

5

{ {75, 76, 65, 87, 87},

{78, 76, 68, 56, 89},

 {67, 87, 78, 77, 65} }

Output

325, 299, 296

Explanation

Out of these subjects, the students average was lowest in Subject 3 i.e., 65 + 68 + 78 = 211/3 = 70.3

So, the teacher will ignore marks of this subject and will consider the total for all the other four subjects for all the three students i.e., 325, 299, 296 respectively.

Hence, {325, 299, 296} is returned as the final output.

Example 2

Input

3

3

{ {50, 30, 70},

{30, 70, 99},

{99, 20, 30} } 

Output

120, 129, 129

Explanation

Out of these subjects, the students average was lowest in Subject 2 i.e., 30 + 70 + 20 = 120/3 = 40

So, the teacher will ignore marks of this subject and will consider the total for all the other two subjects for each of the three students i.e., 120, 129, 129 respectively.

Hence, {120, 129, 129} is returned as the final output.



Input format
input1: An integer value N denoting the number of students

input2: An integer value M denoting the number of subjects

input3: A 2-D integer array of size N*M containing the marks of all students in each subject.

Output format
Return an integer array of size N containing the total marks of each student after deducting the score for that one subject.

'''

n=int(input())
m=int(input())
arr=[]
avg=[]
ans = []
for i in range(n):
    ele=list(map(int,input().split()))
    arr.append(ele)
for i in range(m):
    sum =0
    for j in range(n):
        sum+=arr[j][i]
    avg.append(sum/n)
index=avg.index(min(avg))
for i in range(n):
    arr[i].pop(index)
for i in range(n):
    sum=0
    for j in range(m-1):
        sum+=arr[i][j]
    ans.append(sum)
ans = [str(i) for i in ans]
print(" ".join(ans))