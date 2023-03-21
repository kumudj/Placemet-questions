'''

Mars stone

Problem Statement

Rob has gone to Mars to collect some stones. The bag he is carrying can hold a maximum weight of M. There are M stones weighing from 1 to M in Mars. There are N stones on Mars that are similar to the ones on Earth. Find the number of stones he can bring from Mars such that none of them are similar to any stone on Earth.

Example1

Input

10

3

1 3 5

Output

2

Explanation

Rob collects one of the following stone weight sets: (2, 4), (2, 6) or (2, 8).

Example2

Input

14

4

4 6 8 9

Output

4

Explanation

Rob collects one of the following weight sets: (1, 2, 3, 7) or (1, 2, 3, 5)

Input format
input1: M, denoting the size of the bag and the number of different stone weights present on Mars.

input2: N, denoting the number of common stones on Earth and Mars.

input3: An N element array containing the list of the weights of the common stones.

Output format
Your function should return the maximum unique stones that can be collected from Mars.

'''

def fun(m,n,arr):
    st=[]
    for i in range(1,m+1):
        if i not in arr:
            st.append(i)
    target = m
    for i in range(len(st)):
        target = target-st[i]
        if target <=0:
            break
    return i
m = int(input())
n = int(input())
arr = list(map(int,input().split()))
print(fun(m,n,arr))