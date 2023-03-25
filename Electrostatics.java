/******************************************************************************

Electrostatics

Problem Statement

Doug is found off charge, every now and then he tries do new things. This time he catch up with the Rod pricing of negative and positive charges. How to calculate the maximum net of absolute value of electrostatic field possible in the region due to the Rod. 

Note

Assume, Electrostatic Field =( Absolute value of Total charge ) * 100

Example1

Input

4 3 5

PNP

3

Output

Explanation

The maximum electric charge on the rod is 4-3+5 = 6 units, so the magnitude of the electric field would be 6 * 100 = 600

Example2

Input

2 3

PN

2

Output

100

Explanation

The maximum possible electric charge on the section of the rod is 2-3 = -1 unit, As the magnitude is never negative so |-1| = 1

so the magnitude of the electric field would be 1 * 100 = 100

Input format
Input1: denoting the magnitude of heat change.

Input2: string denoting nature of each charge ith, entry represents sign of charge at ith location in input 1.

Input3: No of changes it holds (length of input 1).

Output format
Return the maximum absolute value of the electrostatic field possible in the rod.
*******************************************************************************/

import java.util.*;
class Main {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String s = sc.nextLine();
        int n = sc.nextInt();
        int charge[] = new int[n];
        int count = 0;
        for(int i=0;i<str.length();i++)
            if(str.charAt(i) != ' ') {
                charge[count] = str.charAt(i)-48;
                count++;
            }
        int sum = 0;
        for(int i=0;i<n;i++) {
            if(s.charAt(i) == 'P')
                sum += charge[i];
            else
                sum -= charge[i];
        }
        if(sum > 0) {
            System.out.println(sum*100);
        }
        else {
            System.out.println(-sum*100);
        }
    }
}