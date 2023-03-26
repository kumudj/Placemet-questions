'''

David and the Training Regimen

Problem Statement

David has adopted a new training regimen. He will do 1, 2 and 3 units of training on the first, second and third day respectively. From the fourth day onwards, the number of units he will train will be equal to the sum of training units done on the previous 3 days. Write a function to return the number of units of training David would do on the Nth day?

Note

Since the answer can be very large, modulo it by 1000000007



Example 1

Input

input1: 4

Output

6

Explanation

Given the above scenario, amount of training units done on the input1th i.e., 4th day is the sum of the training units done on the 1st, 2nd and 3rd day i.e., (1+2+3=6). Hence, 6 is returned as output.

Example 2

Input

input1:

6

Output

20

Explanation

Given the above scenario, amount of training units done on the input 1th day is the sum of the training units done on the 3rd, 4th and 5th day i.e., (3+6+11=20). Hence, 20 is returned as output.



Input format
input1: An integer value denoting the value of Nth day. (1 <= input1 <= 10^9)



Output format
Return the amount of training units done on the input1th day

'''


n=int(input())
units=[]
units.append(1)
units.append(2)
units.append(3)
temp=0
for i in range(3, n):
    temp=units[i - 3]+ units[i-2]+units[i-1]
    units.append(temp)
print(units[n-1])