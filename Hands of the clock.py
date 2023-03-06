'''
Hands of the clock

Problem statement

You are given a string input time = 'AB:CD' where AB denotes the hours from 00 to 12 and CD denotes the minutes from 00 to 59, in a 12-hour format. 

Your task is to write a program to calculate the smallest angle between the hour hand and the minute hand of a clock, for the given time.

Note

Return your answer with up to 1 decimal place

Example 1

Input

09:06

Output

123.0 

Explanation

123.0 degrees is the smallest angle formed between the hour hand and the minute hand at 09:06 a.m or 09:06 p.m

Example 2 

Input

01:56

Output

82.0

Explanation

82.0 degrees is the smallest angle formed between the hour hand and minute hand at 01:56 a.m. or 01:56 p.m
'''

def angle(h,m):
    if h<0 or m<0 or h>12 or m>60:
        print("Wrong input")
    if h==12:
        h=0
    if m==60:
        m=0
        h+=1
        if(h>12):
            h=h-12
    h_a=0.5*(h*60+m)
    m_a=6*m
    angle=abs(h_a-m_a)
    angle=min(360-angle,angle)
    return angle
arr=input()
h=((ord(arr[0])-48)*10)+(ord(arr[1])-48)
m=((ord(arr[3])-48)*10)+(ord(arr[4])-48)
print(angle(h,m))
