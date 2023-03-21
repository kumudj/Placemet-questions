/******************************************************************************

Swapper

Problem Statement

You are given a string which you have to convert into a palindrome such that each step involves swapping two adjacent characters. Find the minimum number of steps it would take for you to do so.

Note

1. If the string could not be converted into a palindrome, return -1. 

2. Also, if the given string is a palindrome, return 0.

Example

Input

ntiin

Output

1

Explanation

The string can be converted to nitin in 1 step by swapping the t and the adjacent i.

Input format
Input1: The string



Output format
The minimum number of steps to convert the string to palindrome, if not possible return -1.

*******************************************************************************/

import java.util.Scanner;
class Main {
    public static boolean isValid(String s) {
        int[] counter = new int[26];
        int oddCount = 0;

        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }
        for (int value : counter) {
            if (value % 2 != 0) {
                oddCount++;
            }
        }
        return oddCount <= 1;
    }

    public static int minSwaps(String inp) {
        if (!isValid(inp)) {
            return -1;
        }

        int n = inp.length();
        char s[] = inp.toCharArray();
        int count = 0;
        for (int i = 0; i < n / 2; i++) {
            int left = i;
            int right = n - left - 1;
            while (left < right) {
                if (s[left] == s[right]) {
                    break;
                } else {
                    right--;
                }
            }
            if (left == right) {
                // s[left] is the character in the middle of the palindrome
                char t = s[left];
                s[left] = s[left + 1];
                s[left + 1] = t;
                count++;
                i--;
            } else {
                for (int j = right; j < n - left - 1; j++) {
                    char t = s[j];
                    s[j] = s[j + 1];
                    s[j + 1] = t;
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inp = scanner.nextLine();
        scanner.close();
        int res = minSwaps(inp);
        System.out.println(res);
    }
}
