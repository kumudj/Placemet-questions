import math
n=int(input())
if(n!=0 and not(n and (n-1))):
    n=int(math.ceil(math.log(n)/math.log(2)));
    print(str(int(math.pow(2,n))));
else:
    n=int(math.ceil(math.log(n)/math.log(2)));
    print(str(int(math.pow(2,n-1))));