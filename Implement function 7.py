'''

You are required to implement the following function

int* MoveZerosToEnd(int* arr, int n);

The function takes an integer array and its length as input. Implement the function to modify the array such that all the 0’s are moved to the end of the array.  

Input format
The first input integer is the size of the array.

The next line of integers is the array elements.

Output format
The output is the modified array with all zeros moved to the right side.

'''

# You are using Python
n=int(input())
arr=list(map(int,input().split()))
zeros=[]
oth=[]
for i in range(n):
    if arr[i]==0:
        zeros.append(0)
    else:
        oth.append(arr[i])
print(*(oth+zeros))