/******************************************************************************
Superior elements

Problem statement

In an array, a superior element is one that is greater than all elements to its right. The rightmost element will always be considered as a superior element. You are given a function,

Int findnumberofsuperiorelements(int* arr, int n);

The function accepts an integer array ‘arr’ and its length ‘n’. Implement the function to find and return the number of superior elements in array ‘arr’.

Example

Input

5

7 9 5 2 8 7

Output

3

Explanation

9 is greater than all the elements to its right, 8 is greater than the element to its right, and 7 is the rightmost element. Hence total 3 superior elements.

Input format
The first integer is the array size.

The next line of integers is the array elements.

Output format
Output is an integer denoting the number of superior elements.

Code constraints
1)     n>0

2)     array index starts from 0.
*******************************************************************************/

import java.util.*;
class Main 
{
    static int findnumberofsuperiorelements(int arr[], int n)
    {
        int c = 1 , j ;
        for(int i = n-2 ; i>=0 ; i--)
        {
            for(j = i+1 ; j<n ; j++)
            {
                if(arr[i]<=arr[j]) break ;
            }
            if(j==n) c++ ;
        }
        return c;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int []arr = new int[n];
        System.out.print(findnumberofsuperiorelements(arr, n));
    }
}