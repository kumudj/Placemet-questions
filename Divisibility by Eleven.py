'''
Divisibility by Eleven

Problem statement

Implement the function

Int divisibilitybyeleven(int num);

The function accepts an integer ‘num’ as input. You have to implement the function such that it returns the number of contiguous integer fragments of ‘num’ that are divisible by 11. Contagious integer fragments of a number, say 1273 are:

1,2,7,3,12,27,73,127,273,and 1273.

Example

Input

1215598

Output

4

Explanation

55,121,12155 and 15598 are contiguous fragments of the number 1215598 that are divisible by 11

Input format
Input is a single integer.

Output format
Output is an integer representing the number of fragments.
'''

def div(num):
    str_num=str(num)
    count=0
    for i in range(len(str_num)):
        for j in range(len(str_num)):
            my_num=str_num[i:j+1]
            if my_num!='':
                if int(my_num)%11==0:
                    count+=1
    return count
num=int(input())
print(div(num))