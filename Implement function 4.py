'''

You are required to implement the following function

int OperationChoices(int c, int n, int a , int b ); 

The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return. 

( a + b ) , if c=1 
( a - b ) , if c=2 
( a * b ) , if c=3 
(a / b) , if c =4 
Assumption

All operations will result in integer output. 

Example

Input 

c :1 

a:12 

b:16 

Output

Since ‘c’=1 , (12+16) is performed which is equal to 28 , hence 28 is returned. 

Input format
The three input integers are the values of c, a and b respectively.

Output format
The output integer is the result of operations performed between a and b.

'''

arr=list(map(int,input().split()))
if arr[0]==1:
    print(arr[1]+arr[2])
elif arr[0]==2:
    print(arr[1]-arr[2])
elif arr[0]==3:
    print(arr[1]*arr[2])
elif arr[0]==4:
    print(arr[1]//arr[2])
else:
    print()
    