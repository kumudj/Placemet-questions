'''
Problem statement

You are provided with 3 numbers: input1, input2, and input3. Each of these is four-digit numbers within the range >=1000 and <=9999 i.e. 

1000 <= input1 <= 9999 

1000 <=input2 <= 9999 

1000 <=input3 <= 9999 

You are expected to find the Key using the below formula 

Key = [SMALLEST digit in the thousands place of all three numbers] 

[LARGEST digit in the hundreds place of all three numbers] [SMALLEST digit in the tens place of all three numbers] [LARGEST digit in the units place of all three numbers]

Given three numbers, write an algorithm to find the key using the above-mentioned formula.

Example 

Input

3521 2452 1352

Output

1522

Explanation

Key = [smallest digit in the thousands place of all three numbers] [LARGEST digit in the hundreds place of all three numbers] [smallest digit in the tens place of all three numbers] [LARGEST digit in the units place of all three numbers] 

If input1 = 3521, input2=2452, input3-1352, then Key = [1][5][2][2] = 1522.

'''

input=list(map(str,input().split()))
a=input[0]
b=input[1]
c=input[2]
one=[a[0],b[0],c[0]]
ten=[a[1],b[1],c[1]] 
hun=[a[2],b[2],c[2]]
tho=[a[3],b[3],c[3]]
r1=str(min(one))
r2=str(max(ten))
r3=str(min(hun))
r4=str(max(tho))
result=[r1,r2,r3,r4]
print("".join(result))
