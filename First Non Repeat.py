# You are using Python
n=input()
u=0
for i in range(len(n)):
    if n.count(n[i]) == 1:
        print(n[i])
        u=1
        break
if(u==0):
    print("0")