'''

Andrew manages a pipe warehouse. He wishes to automate the process of transferring the pipes from the warehouse to the carrier truck. There are N pipes in the warehouse placed vertically along a wall. In the automated system, a drone picks the pipes by length and carries them to the carrier truck. In each turn, the drone moves from left to right to find the pipes whose lengths are greater than the pipe on their left. After finding the pipe, the drone takes the pipe to the carrier truck. The drone repeats this process until it has no more pipes to pick.

Write an algorithm to output the list of pipes that will remain in the warehouse after the drone has completed this process.

Example

Input

5 

3 2 4 6 5

Output

3 2

Explanation

In the first turn, the drone picks the pipe with length 4 as 4 > 2. So, the remaining pipes are 3, 2, 6, and 5.

In the next turn, the drone picks the pipe with length 6 as 6 > 2. So, the remaining pipes are 3, 2, and 5.

In the next turn, the drone picks the pipe with length 5 as 5 > 2. So, the remaining pipes are 3 and 2.

Input format
The first line of the input consists of an integer - numOfPipes, representing the number of pipes in the warehouse (N).

The second line consists of N space-separated integers - len[0], len[1], .... len[N-1], representing the length of the pipes.

Output format
Print space-separated integers representing the list of the remaining pipes in the warehouse.


'''

n=int(input())
arr=list(map(int,input().split()))
m=arr.index(min(arr))
print(str(arr[0]),end=' ')
temp=arr[0]
for i in range(1,n):
    if arr[i]<temp:
        print(arr[i],end=" ")
        temp=arr[i]
