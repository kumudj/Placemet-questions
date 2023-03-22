/******************************************************************************

Total occurrence

Problem Statement

Given two integer numbers input1 and input2, find the total number of occurrences of input1 in a series of natural numbers from 0 till input2.

Note:

input1 will be within 1-9 and
input2 will be within 1-100.
Implement given function:

public int findTotalOccurrence(int input1, int input2)

Example1

Input

2

20

Output

3

Explanation

Number 2 is repeated 3 times in the series of natural numbers from 0 - 20 i.e at 2, 12, 20.

Example2

Input 

2

30

Output

13

Explanation

Number 2 is repeated 13 times in the series of natural numbers from 0 - 30 i.e at 2, 12, 20, 21, 22 (occurred twice) 23, 24, 25, 26, 27, 28, 29.



Input format
input 1: Integer represents occurrence value

input 2: Integer value represents N

Output format
Refer sample output
*******************************************************************************/

import java.util.*;
class Main
{
    public static int findTotalOccurrence(int n, int x)
    {
        int m , t = 0 ; 
        while(n>=1)
        {
            m = n ;
            while(m!=0)
            {
                if(m%10 == x)
                    t++ ;
                m /= 10 ;
            }
            n-- ;
        }
        return t ;
    }
	public static void main(String[] args) 
	{
	    Scanner sc=new Scanner(System.in);
	    int m= sc.nextInt(); 
	    int n = sc.nextInt();   
		System.out.print(findTotalOccurrence(n,m));
	}
}