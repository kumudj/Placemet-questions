/******************************************************************************

Reverse Bits

Problem Statement

Given a 32-bit signed integer, write a function to return the integer formed by reversing its bits.

Example1

Input

2

Output

1073741824

Explanation

The 32-bit equivalent of 2 is: 00000000 00000000 00000000 00000010. On reversing its bits, we get, 01000000 00000000 00000000 00000000 which is the binary equivalent of 1073741824. Hence, the output is 1073741824.

Example2

Input

1

Output

-2147483648

Explanation

The 32-bit equivalent of 1 is: 00000000 00000000 00000000 00000001. On reversing its bits, we get, 10000000 00000000 00000000 00000000 which is the binary equivalent of -2147483648. Hence, the output is -2147483648.

Input format
input1: A 32-bit signed integer value.

Output format
Return the signed integer value formed by reversing the bits of input1.
*******************************************************************************/

import java.util.*;
import java.lang.Math;
class Main
{
    public static int reverse(int n)
    {
        int result = 0;
        for(int i=0;i<32;i++)
        {
            result <<= 1;
            result |= n & 1;
            n >>= 1;
        }
        return result;
    }
	public static void main(String[] args) 
	{
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
		System.out.println(reverse(n));
	}
}
