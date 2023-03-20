'''

The Difference

Problem Statement

Ron and Susan have been paired together to complete a piece of homework given to them by their teacher. Ron selects the longest palindromic substring of a string and Susan selects the shortest palindromic substring of the same string. They got tired after doing this task and have asked you to calculate the difference between the lengths of these strings as they have to chart it and submit it to their teacher.

Example1

Input

level

Output

4

Explanation

The longest palindromic sub-string will be "level" with length 5 and the shortest can be “I” will be length 1. So, the difference is 5-1 = 4.

Example2

Input

abac

Output

2

Explanation

The longest palindromic sub-string will be "aba" with length 3 and the shortest can be "a" with length 1. So the difference is 3-1 = 2.

Input format
Input: The string they have been given.

Output format
The difference between the lengths of the strings found by Ron and Susan
'''

def fun(string):
    substr=[string[i:j] for i in range(len(string)) for j in range(len(string)+1)]
    pal=[]
    for i in range(len(substr)):
        s=substr[i]
        if s==s[::-1]:
            pal.append(s)
    count=[]
    for i in range(len(pal)):
        count.append(len(pal[i]))
    count=[i for i in count if i !=0]
    return max(count)-min(count)
string=input()
print(fun(string))
        
