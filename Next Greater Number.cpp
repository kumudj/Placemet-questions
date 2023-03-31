/******************************************************************************

Next Greater Number

Problem Statement

Given a number 'N' (containing at most 10,000 digits), find the next greater number having the same digits. 

It is guaranteed that there exists a next greater number having the same digits as N.

Example 1

Input

3

182

Output

218

Explanation

Using the same digit the number of permutations are:

1. 128

2. 218

3. 281

4. 812

5. 821

The next greatest number for 182 is 218.

Example 2

Input

19

1234567849876554321

Output

1234567851234456789

Input format
input1: the length of the String 'N'

input2: the number 'N' in the form of a string.

Output format
Return the next greater number having the same digits as 'N' in the form of a string.

*******************************************************************************/
#include<bits/stdc++.h>
using namespace std;

void swap(char *a, char *b)
{
    char temp = *a;
    *a = *b;
    *b = temp;
}

void findNext(char number[], int n)
{
    int i, j;
    for (i = n-1; i > 0; i--)
        if (number[i] > number[i-1])
           break;
   /* if (i==0)
    {
        cout << "Next number is not possible";
        return;
    }*/
    int x = number[i-1], smallest = i;
    for (j = i+1; j < n; j++)
        if (number[j] > x && number[j] < number[smallest])
            smallest = j;
    swap(&number[smallest], &number[i-1]);
    sort(number + i, number + n);
    cout << number;
 
    return;
}

int main()
{
    int n;
    cin >> n;
    char digits[n];
    cin >> digits;
    findNext(digits, n);
    return 0;
}