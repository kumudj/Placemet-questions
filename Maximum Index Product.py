'''
Maximum Index Product

Problem statement

Implement the following function

int maxindexproduct(int* arr, int n);

The function accepts an integer array ‘arr’ of size n. Implement the function to find and return maximum index product. For every index ‘j’, index product = left(j) x right (j). Left(j) = an index ‘k’ which is closest to index ‘j’ , such that k < j and arr[k] > arr[j], if no such index ‘k’ exists then left(j) = 0. Right(j) = an index ‘i’ which is closest to index ‘j’ , such that i>j and arr[i] > arr[j] , if no such index ‘i’ exists then right(j) = 0.

Note

Return -1 if the array is empty (or none in the case of python)

Indexing starts from 0.

Example

Input

7 // input size

-3 4 3 6 4 5 -2

Output

15

Explanation

Index product

Index product of index 0=0x1=0

Index product of index 1=0x3=0

Index product of index 2=1x3=3

Index product of index 3=0x0=0

Index product of index 4=3x5=15

Index product of index 5=3x0=0

Index product of index 6=5x0=0

The maximum index product is 15. Thus, the output is 15.

Input format
The first integer is the size of the array.

The next line of integers is the elements of the array.

Output format
Output is the max index product.

Code constraints
Element at index 0 is the smallest.

'''

# You are using Python
def product(arr,n):
    max=-99999
    for i in range(1,n-1):
        index=0
        for j in range(i-1,-1,-1):
            if arr[j]>arr[i]:
                index=j
                break
        indexx=0
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                indexx=j
                break
        prod=index*indexx
        if prod>max:
            max=prod
    return max
n=int(input())
arr=list(map(int,input().split()))
print(product(arr,n))