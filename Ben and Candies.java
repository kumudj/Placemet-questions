/******************************************************************************

Ben and Candies

Problem Statement

Ben has been provided with N number of candies which are kept on a table one after the other. The flavor of each candy is denoted by an integer A[i]. Although he loves eating candies but hates to eat the candies of the same flavor more than once. He has defined a few rules to eat the candies:

Ben can start eating candies from any candy kept on the table.
Once he starts eating the candies, he cannot skip any candy.
For example: Let's say first he eats a candy at index i then he will have to eat candies at index i+1, i+2...... and so on either till the candy with the same flavor occurs or no more candies are left. Once a candy of a flavor which is already eaten occurs, he will stop eating the candies. Your task is to find and return the maximum number of candies Ben can eat considering the above scenario.

Note: Once he eats a candy at index i, he cannot eat a candy which occurs before index i, he will only go in forward direction, to eat the candies.

Example1

Input

3

1 2 3

Output

3

Explanation

In this case, all the candies have a unique flavor. So, Ben starts eating candies from index 0 and eats all the candies that are kept on the table. So, in total he eats 3 candies. Therefore 3 is returned as the output.

Example2

Input

5

1 2 2 3 5

Output

3

Explanation

Ben can either eat candies at indices 0 and 1 or he can eat the candies starting from index 2 till index 4. On choosing the latter, he will be able to eat a greater number of candies. So, he can eat a maximum of 3 candies. Therefore, 3 will be returned as the output.

Input format
input1: An integer value N denoting the number of candies

input2: An integer array of length N, where each value denotes the flavor of a candy.

Output format
Return the maximum number of candies that Ben can eat, considering the given scenario.

*******************************************************************************/

import java.util.*;
class Main {
	public static int maxUniqueNum(int arr[],int N)
	{
		int maxUnique = 0;
		for (int i = 0; i < N; i++) 
		{
			int currentUnique = 0;
			HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
			for (int k = i; k < N; k++) 
			{
				if (!map.containsKey(arr[k])) 
				{
					map.put(arr[k], 1);
					currentUnique++;
				}
				else
				{
				    break;
				}
			}
			if (currentUnique > maxUnique)
				maxUnique = currentUnique;
		}
		return maxUnique;
	}
	public static void main(String[] args)
	{
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    int[] arr = new int[n];
	    for(int i=0;i<n;i++)
	        arr[i]=sc.nextInt();
		System.out.println(maxUniqueNum(arr,n));
	}
}