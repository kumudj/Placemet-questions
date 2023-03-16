'''
Push Zeros to end

Problem statement

Write a function to push all the zeros that are present to the end of the array. The respective order of other elements should remain the same.

Example 1

Input

input1: {5, 0, 7, 6}

input2: 4

Output

{5, 7, 6, 0}

Explanation

On Shifting the zeros to the end, the array will change from {5, 0, 7, 6} to {5, 7, 6, 0}.

Example 2

Input

input1: {0, 3, 0, 2, 0}

input2:

Output

{3, 2, 0, 0, 0}

Explanation

On Shifting the zeros to the end, the array will change from {0, 3, 0, 2, 0} to {3, 2, 0, 0, 0}.

Input format
input1: Array elements

input2: Integer N, Array Size

Output format
Return the array containing non-zero elements first followed by the zeroes.

'''



def fun(arr):
    zero = []
    non = []
    for i in range(len(arr)):
        if(arr[i] == 0):
            zero.append(arr[i])
        else:
            non.append(arr[i])
    return non+zero
n = int(input())
arr = list(map(int, input().split()))[:n]
res = fun(arr)
print(*res)