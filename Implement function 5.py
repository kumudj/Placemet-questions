'''

You are required to implement the following function

void replaceCharacter(string str, char ch1, char ch2); 

The function accepts a string ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments. Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in the original string are replaced by ‘ch2’ and all occurrences of ‘ch2’ in the original string are replaced by ‘ch1’. 

Assumption

String Contains only lower-case alphabetical letters. 

Note

Return null if the string is null. 
If both characters are not present in the string or both of them are the same, then return the string unchanged. 
Example

Input

Str: apples 

ch1:a 

ch2:p 

Output

paales 

Explanation

‘a’ in the original string is replaced with ‘p’ and ‘p’ in the original string is replaced with ‘a’, thus output is paales. 

Input format
The first input is the string.

The next two char inputs are ch1 & ch2 respectively.



Output format
Output is the modified string.

'''

def swap (user_input, str1, str2): 
    result = '' 
    if user_input != None: 
        result = user_input.replace(str1, '*').replace(str2, str1).replace('*', str2) 
        return result 
    return 'Null' 
user_input = input() 
str1, str2 = map(str,input().split()) 
print(swap(user_input, str1, str2)) 
    