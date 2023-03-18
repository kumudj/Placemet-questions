'''
Problem statement

Design a way to sort the list of positive integers in descending order according to the frequency of the elements. The elements with higher frequency come before those with lower frequency. Elements with the same frequency come in the same order as they appear in the given list.

Example

Input

19

1 2 2 3 3 3 4 4 5 5 5 5 6 6 6 7 8 9 10

Output

5 5 5 5 3 3 3 6 6 6 2 2 4 4 1 7 8 9 10

Explanation

The number with highest frequency appears first.

If two numbers have equal frequency the number which appears first in the array has to be printed.

Input format
The first line of the input consists of an integer num, representing the number of elements in the list(N).

The second line consists of N space-separated integers representing the elements in the list.

Output format
Print N space-separated integers representing the elements of the list sorted according to the frequency of elements present in the given list.

'''

def sortByFreq(arr, n):
    maxE = -1
    for i in range(n):
        maxE = max(maxE, arr[i])
    freq = [0] * (maxE + 1)
    for i in range(n):
        freq[arr[i]] += 1
    cnt = 0
    for i in range(maxE + 1):
        if freq[i] > 0:
            value = 100000 - i
            arr[cnt] = 100000 * freq[i] + value
            cnt += 1
    return cnt
def printArray(arr, cnt):
    for i in range(cnt):
        frequency = arr[i] / 100000
        value = 100000 - (arr[i] % 100000)
        for j in range(int(frequency)):
            print(value, end = " ")
n = int(input())
arr = list(map(int, input().split()))
cnt = sortByFreq(arr, n)
arr.sort(reverse = True)
printArray(arr, cnt)