'''

Escape from Jail

Problem Statement

A thief, Jack Sparrow plans to escape from jail. He, being a monkey man, can jump over a wall. Jack has practiced well and succeeds in jumping X meters. However, the wall is slippery, so he slides down Y meters after every jump. To escape from jail, he must cross N number of walls, where the height of each wall is given in an array. Your task is to return the total number of jumps Jack needs to make to escape from the jail.

Example1

Input

10

1

1

10

Output

1

Explanation

Here, Jack Sparrow can jump a height of 10 meters but slides down by 1 meter. He has 1 wall of jump, and the height of the wall is 10 meters. Since he jumps 10 meters in the first attempt, he crosses the wall easily in the first attempt itself. Therefore, 1 is returned as the output.

Example2

Input

5

1

2

9 10

Output

5

Explanation

Here, Jack Sparrow can jump a height of 5 meters but slides down by 1 meter. He has 2 walls to jump, and the height of each wall is 9 and 10 meters respectively.

First wall:

Jack makes 2 attempts, because at the first attempt he jumps 5 meters, but slides down by 1 meter and does not cross the wall.

In the next attempt, he jumps 5 more meters from that position, and this time he does not slide down and crosses the wall in this attempt (4+5=9)

Second wall:

Jack takes 3 attempts because, at the second attempt on this wall, he slides down by 1 meter. So, 4+5=9, and the height of the wall is 10 meters. At his third attempt, Jack Sparrow is able to escape from jail. So, a total of 5(2+3) attempts are made. Therefore 5 is returned as the output.

Input format
input1: An integer value X denoting the number of meters he can jump up (1 <= input1 <= 10^4)

input2: An integer value Y denoting the number of meters he slides down (1 <= input2 <= 10^4)

input3: An integer value N denoting the number of walls he needs to jump to escape (1 <= input3 <= 10^4)

input4: An integer array of size N representing the height of each wall where (1 <= input4[i] <= 1000)

Output format
Return an integer value representing the total number of jumps Jack Sparrow must make in order to escape from the jail.
'''


x=int(input())
y=int(input())
n=int(input())
w=list(map(int,input().split()))
js=0
for i in range(n):
    r=x
    j=1
    while r<w[i]:
        r+=(x-y)
        j+=1
    js+=j
print(js)