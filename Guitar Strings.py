'''
Guitar Strings

Problem statement

Alice has a guitar with N strings. Each string can play x[i] songs before the string snaps. Alice decided that each day in the next N days, she will pick a string and keep playing on it until the string snapped.

Alice earns money for every song when she plays on her guitar. On the ith day (0 <= i < N), Alice earns (N-i) coins for each song she plays.

Your task is to find the maximum amount of coins Alice can earn

Example 1

Input

3

3

9 

5

Output

40

Explanation

The best way is to use the second string on the first day, the last string on the second day, and finally, the first string on the last day. This will give 40. 9 * 3 + 5 * 2 + 3 * 1.

Example 2

Input

5

9

2

5

10

6

Output

116

Explanation

The best order of the strings is [3, 0, 4, 2, 1] and it will result in 116 coins.

'''

n=int(input())
arr=[]
add=0
for i in range(n):
    ele=int(input())
    arr.append(ele)
arr.sort()
for i in range(1,n+1):
    add+=(i*arr[i-1])
print(add)