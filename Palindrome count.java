/******************************************************************************

Palindrome count

Problem Statement

Write a function to find all the words in a string which are palindrome.

Note

A string is said to be a palindrome if the reverse of the string is the same as string. For example, "abba” is a palindrome, but "abbc" is not a palindrome.

Example1

Input

this is level 71

Output

1

Explanation

The reverse of the word "level" is "level". Hence, the word is a palindrome. As the string contains only one palindrome, so the returned value will be 1.

Example2

Input

hello world 

Output

0

Explanation

No palindrome string in the sentence so print 0.

Input format
Input1: string 

Output format
Return the number of palindromes in the given string

*******************************************************************************/

import java.util.*;
class Main 
{
	static boolean checkPalin(String word)
	{
		int n = word.length();
		word = word.toLowerCase();
		for (int i=0; i<n; i++,n--)
		if (word.charAt(i) != word.charAt(n - 1))
			return false;	
		return true;
	}
	static int countPalin(String str)
	{	
		str = str + " ";
		String word = "";
		int count = 0;
		for (int i = 0; i < str.length(); i++)
		{
			char ch = str.charAt(i);
			if (ch != ' ')
				word = word + ch;
			else {
				if (checkPalin(word))
					count++;
				word = "";
			}
		}
		return count;
	}
	public static void main(String args[])
	{
	    Scanner sc=new Scanner(System.in);
	    String s=sc.nextLine();
		System.out.println(countPalin(s));
	}
}