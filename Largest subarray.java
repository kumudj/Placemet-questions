/******************************************************************************

Largest subarray

Problem Statement

Given an array containing only 0s and 1s, find the length of the largest subarray containing an equal number of 0s and 1s.

Example1

Input

4

1 1 0 1

Output

2

Explanation

Largest possible array here would be of length 2 as there should be equal number of 0 and 1 in it. The starting index and ending index of the largest subarray is 1 and 2. Hence the output is 2.

Example2

Input

5

1 1 1 1 1

Output

0

Explanation

In the above example, there are no 0s in the array. Hence the output is 0.

Input format
input1: N, the length of an array

input2: Array containing 0s and 1s

Output format
Return the length of the largest sub-array containing equal no. of 0s and 1s

*******************************************************************************/
import java.util.*;
class Main
{
    public static int findSubArray(int arr[], int n)
    {
    	int sum = 0;
    	int maxsize = -1, startindex;
    	for (int i = 0; i < n - 1; i++) 
    	{
    		sum = (arr[i] == 0) ? -1 : 1;
    		for (int j = i + 1; j < n; j++) 
    		{
    			if(arr[j] == 0)
    			    sum+=-1;
    			else
    			    sum += 1;
                if (sum == 0 && maxsize < j - i + 1) 
                {
    				maxsize = j - i + 1;
    				startindex = i;
    			}
    		}
    	}
    	if (maxsize == -1)
    		return 0;
    	else
    		return maxsize;
    }
    public static void main(String[] args) 
	{
	    Scanner sc=new Scanner(System.in);
	    int n= sc.nextInt(); 
	    int[] arr=new int[n];
	    for(int i=0;i<n;i++)
	        arr[i]=sc.nextInt(); 
		System.out.print(findSubArray(arr,n));
	}
}