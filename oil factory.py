'''

An oil factory has N number of containers and each has a different capacity. During the renovation, the manager decided to make some changes to the containers. He wishes to make different pairs for the containers in such a way that in the first pair, the container of maximum capacity is paired with the container of minimum capacity, and so on for the rest of the containers, to maintain a balance throughout all the pairs of containers.

Write an algorithm to make different pairs of containers in such a way that the first container in the pair is of maximum capacity and the second container in the pair is of minimum capacity.

Note

If only one container is left and no pair is possible then print the capacity of that container and the second value will be '0'.

Example

Input

6

100 560 23 19 53 20

Output 

560 19

100 20

53 23

Input format
The first line of the input consists of an integer - numContainers, representing the number of containers (N).

The next line consists of N space-separated integers - cont1, cont2, .... contN, representing container capacity.

Output format
Print K lines consisting of two space-separated integers representing the pairs that will be formed to maintain the balance by pairing the container of maximum capacity with the container of minimum capacity and so on.



'''

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for i in range(n//2):
    print(str(arr[-(i+1)])+" "+str(arr[i]))
if n%2!=0:
    print(str(arr[n//2])+" "+"0")
