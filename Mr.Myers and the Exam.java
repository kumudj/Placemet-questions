/******************************************************************************

Mr.Myers and the Exam

Problem Statement

A mathematics question paper has certain number of questions and each question is assigned some random maximum marks. 

Mr. Myers wants to edit the marks assigned to the questions such that:

1. All questions in the paper should have distinct maximum marks.

2. The total marks of all the questions should be as low as possible.

Mr. Myers wants to achieve this by making minimal changes in the original format, assigning the question at least as many marks as it originally had. Find the minimum total marks that he can set the paper for.

Example1

Input

5

1 2 3 4 5

Output

15

Explanation

As all the questions already have distinct marks, he can set the paper as it is with minimum marks as 1+2+3+4+5=15.

Example2

Input

5

1 4 5 4 5

Output

23

Explanation

Here, the question 1 would have at least 1 mark, question 2 would have at least 4 marks, question 3 would have atleast 5 marks, so the new set of marks will have to be {1, 4, 5, 6, 7}, such that all the conditions are satisfied.

Input format
input1: The number of questions in the paper

input2: The array representing the original marks assigned to every question



Output format
The minimum total marks Mr. Myers can set the paper for

*******************************************************************************/

import java.util.*;
class Main
{
   public static int minimal(int N,int[] a)
   {
       int temp=0;
       HashMap<Integer,Boolean> m = new HashMap<>();
       for(int i=0;i<N;i++)
        {
            while(m.containsKey(a[i]))
            {
                temp=a[i];
                a[i]+=1;
            }
            m.put(a[i],true);
        }
        int sum = 0;
        for(int i=0; i<N;i++)
            sum +=a[i];
    return sum;
    }
    public static void main(String[] args) 
    {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] a=new int[N];
    for(int i=0;i<N;i++)
        a[i]=sc.nextInt();
    System.out.print(minimal(N,a));
    }
}


