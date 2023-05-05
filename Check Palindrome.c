/******************************************************************************

Write a program to check if a string is palindrome or not without reversing a string.

Input format
String

Output format
Palindrome or Not Palindrome

Note : Output is case and space sensitive

*******************************************************************************/
// You are using GCC
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    string s,o;
    cin >> s;
    o=s;
    reverse(s.begin(), s.end());
    if(s==o)
    {
        cout << "Palindrome\n";
    }
    else{
        cout << "Not Palindrome\n";
    }
}