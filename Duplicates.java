/******************************************************************************

Duplicates

Problem Statement

Write a function to remove duplicate elements from an array and return the array with unique integer values only.

Example1

Input

6

11 11 11 13 13 20

Output

11 13 20

Explanation

As in the above array, 11, 13 and 20 are the unique integers. So the output is {11, 13, 20}

Example2

Input

3

11 14 25

Output

11 14 25

Explanation

As in the above array, all the integers are unique. So the output remains the same as in the input

Input format
input1: Length of the above integer array

input2: An integer array containing numbers

Output format
Return an integer array after removal of duplicate values

*******************************************************************************/
import java.util.*;
class Main
{
	static void removeDups(int[] arr, int n)
	{
		HashMap<Integer,Boolean> mp = new HashMap<>();
		for (int i = 0; i < n; ++i)
		{
			if (mp.get(arr[i]) == null)
				System.out.print(arr[i] + " ");
			mp.put(arr[i], true);
		}
	}
	public static void main(String []args)
	{
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    int[] arr=new int[n];
	    for(int i=0;i<n;i++)
	        arr[i]=sc.nextInt();
		removeDups(arr, n);
	}
}