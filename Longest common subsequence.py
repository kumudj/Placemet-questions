'''
Longest common subsequence

Problem statement

Given two strings, 'x' and 'y' (1 <= length(x), length(y) <= 1000), find the length of their Longest Common subsequence (LCS). The strings contains only lowercase letters.

Write a program that takes in two string inputs and returns the length of their LCS.

Example 1

Input

input1: aba 

input2: ababa

Output

3

Explanation

The length of the longest common subsequence is 3 that is "aba".

Example2

Input

input1: aggtab 

input2: gxtxayb

Output

4

Explanation

The length of the longest common subsequence is 4 that is "gtab"

Input format
input1: input string 'x'

input2: input string 'y'

Output format
Return the length of the LCS of 'x' and 'y'.
'''

def lcs(x,y,m,n,dp):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    if x[m-1]==y[n-1]:
        dp[m][n]=1+lcs(x,y,m-1,n-1,dp)
        return dp[m][n]
    dp[m][n]=max(lcs(x,y,m,n-1,dp),lcs(x,y,m-1,n,dp))
    return dp[m][n]
str1=input()
str2=input()
m=len(str1)
n=len(str2)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
print(lcs(str1,str2,m,n,dp))