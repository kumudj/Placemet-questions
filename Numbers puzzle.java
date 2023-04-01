/******************************************************************************

Numbers puzzle

Problem Statement

Give a set of number, one can arrange them in any order, but must pay a penalty equal to the sum of the absolute difference between adjacent numbers. Return the minimum penalty that must be paid .

Example1

Input

3

1 3 2

Output

2

Explanation

The order that incurs the minimum penalty is 1, 2, 3. The penalty is abs(2-1) + abs(3-2) = 2

Example2

Input

4

1 6 -2 4

Output

8

Explanation

The order that incurs the minimum penalty is -2, 1, 4, 6. The penalty is abs(6-4) + abs(4-1) + abs(1-(-2)) = 2 + 3 + 3 = 8.

Input format
input1: length of an integer array of number (2<=input 1<=1000) .

input2 : integer array (1<=input 2[i]<=10000).

Output format
Return the minimum penalty

*******************************************************************************/
import java.util.*;
import java.lang.Math;
public class Main
{
    public static int sumPairs(int arr[],int n)
    {
        Arrays.sort(arr);
    	int sum = 0;
    	for (int i=1; i<n; i++)
    		sum += Math.abs(arr[i-1] -arr[i]);
    	return sum;
    }
	public static void main(String[] args) 
	{
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    int arr[]=new int[n];
	    for(int i=0;i<n;i++)
	        arr[i]=sc.nextInt();
		System.out.print(sumPairs(arr,n));
	}
}

