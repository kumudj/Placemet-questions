'''
Problem statement

Base number

The alphabetical order of letters is their base number. i.e , base number of A=1,B=2,C=3,D=4 and so on.

Implement the given function

Static string decodemessage(string msg){ }

The function accepts a string ‘msg’ as its argument. ‘msg’ contains an encoded message, where encoded characters are separated with a space. Implement the function to find and return the decoded message that has been encoded as follows:

Each letter was converted to its base number
A space is converted to an underscore( _ )
number is preceded by the number symbol ( # )
Note

[1]   Return all letters in upper case

[2]   Return space in decoded message only when underscore symbol ( _ ) appears in ‘msg’

[3]   If ‘msg’ is empty or “NULL” return “NULL”.

Example

Input

2 1 4 _ 3 1 20 @ # 459

Output

BAD CAT @459
'''

def decode(s):
    flag = 0
    #l=['1','2','3','4','']
    for i in range(len(s)):
        if(s[i]=='#'):
            flag = 1 
            continue 
        if(s[i] == '_'):
            print(" ",end="")
        elif(s[i] == ' '):
            continue
        elif((flag == 0) and s[i].isdigit()):
            print(chr(int(s[i])+64),end="")
        elif((flag == 1) and s[i].isdigit()):
            print(s[i],end="")
        else:
            print(s[i],end="")
s=list(map(str,input().split()))
decode(s)
