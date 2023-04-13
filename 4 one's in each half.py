'''

Given a 2-d matrix having 1 and 0, can you perform a single cut on matrix horizontally or vertically such that both 2 halves have an equal number of 1's. (Medium)



 Example : 

 Input 



1 1 1 1

1 0 0 1

0 0 0 1

0 1 0 0



Output 



Yes



Explanation: You can do cut vertically such that 2 halves will have an equal number of 1's (4 one's in each half)



1 1  1 1

1 0  0 1

0 0  0 1

0 1  0 0
'''

n=int(input())
arr=[]
for i in range(n):
    ele=list(map(int,input().split()))
    arr.append(ele)
s,k,p,q=0,0,0,0
for i in range(n):
    for j in range(n//2):
        if arr[i][j]==1:
            s+=1
    for j in range(n//2,n):
        if arr[i][j]==1:
            k+=1
    for j in range(n//2):
        if arr[j][i]==1:
            p+=1
    for j in range(n//2,n):
        if arr[j][i]==1:
            q+=1

if s==k or p==q:
    print('Yes')
else:
    print('No')
        
