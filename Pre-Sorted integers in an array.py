'''
Pre-Sorted integers in an array

Problem statement

You are given an array of integers, arr, of size array_length. Your task is to find the number of elements whose positions will remain unchanged when arr is sorted in ascending order.

For example, let arr = {1, 3, 2, 4, 5}. If arr were to be sorted in ascending order, it would appear as {1, 2, 3, 4, 5}. By inspection, the integers 1, 4 and 5 do not change position before and after sorting. Hence, in this example, there are 3 elements whose position will remain unchanged when arr is sorted in ascending order.

Example 1

Input

1 

10

Output

1

Explanation

There is only one element in arr. Hence arr is already sorted, and the position of that one element in arr is in sorted order. Thus, the output is 1.

Example 2

Input

5

5

4

3

2

1

Output

1

Explanation

arr = {5, 4, 3, 2, 1}. When sorted, it becomes {1, 2, 3, 4, 5}. By inspection, the third element in arr, 3, does not change its order, hence the output is 1.

Input format
The first line contains an integer, array_length, denoting the number of elements in arr.

Each line i of the array_length subsequent lines (where 0 <= i < array_length) contains an integer describing arr[i]

Output format
The output prints an integer denoting the number of elements whose positions will remain unchanged when arr is sorted in ascending order as specified in the problem statement.

'''

def fun(arr,temp,n):
    count=0
    temp.sort()
    for i in range(n):
        if arr[i]==temp[i]:
            count=count+1
    return count
n=int(input())
arr=[]
temp=[]
for i in range(n):
    arr.append(int(input()))
    temp.append(arr[i])
print(fun(arr,temp,n))