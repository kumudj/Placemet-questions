'''

Transmit a Message

Problem statement

Professor X has developed a new machine to transmit messages. The machine accepts a message in the form of a string of characters and transmits it to another machine of the same type at some other location. However, the machine has a certain bug. It can transmit only one type of character. As soon as it encounters a different type of character, the message recorded till that point is erased and the machine starts recording a new message beginning from that character.

Professor X wants to send the longest message possible to his friend. To do this, he can stop the machine at any point and transmit the message by pressing the send button. However, he can do this only when the machine is in the recording mode and not the erasing mode. He wants your help.

Given the input string, your task is to find the longest possible message that can be delivered by the machine. If there is more than one longest possible message, find the message which is nearer to the end of the string.

Example 1

Input

abb

Output

2

bb

Explanation

The acceptable string is abb, the machine records 'a'. then encounters an unacceptable character 'b'. so the previous message is lost and the new message starts with 'b' and finally when it encounters the same character, the final message is 'bb'. Thus the output1 is 2 and output2 is 'bb'.

Example 2

Input

aabbddd

Output

3

ddd

Explanation

The acceptable string is aabbddd, the machine records 'a' then encounters another 'a' thus the message becomes 'aa'. After this, the machine encounters 'b', so the previous message is lost and the new message starts with 'b', and in the same manner, the final message is 'ddd'. Thus the output1 is 3 and output2 is 'ddd'.

Input format
The original string message.

Output format
The first output is an integer denoting the length of the longest possible message.

The second output is a string denoting the longest possible message.
'''

# You are using Python
def fun(s):
    l = 0
    ml = 0
    ind = 0
    for i in range(len(s) - 1):
        l = 1
        while s[i] == s[i+1]:
            l += 1
            i+=1
            if i+1 == len(s):
                break
        if l >= ml:
            ml = l
            ind = i- l + 1
    print(ml)
    str = ""
    i = ind
    j =0 
    k = 0
    while j<ml:
        str += s[i]
        j += 1
        k += 1
        i += 1
    return str
s = input()
print(fun(s))
        