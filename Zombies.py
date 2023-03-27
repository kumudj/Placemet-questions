'''

Zombies

Problem Statement

In a country of zombies, each city has a certain percentage of zombies. Cities are designated as 0 to n-1.

1. A city[i] is 'magical' if city[i] and city[i+1] have no common divisor other than 1.

2. A city[i] is 'good' if the percentage of zombies in the city[i] is more than percentage of zombies in city[i+1].

Find a city that is perfect, where perfect means both good and magical If there are more than one perfect cities, output the left-most city index. Also, the minimum number of cities in a country is 2 and there will be atleast one perfect city.

Example1

Input

1 1 3 6 7 3

6

Output

4

Explanation

The city at index 4 is a perfect city, as input1[4] and input1[5] are co-prime. Also, input1[4] has a larger percentage of zombies than its neighboring city input1[5].

Example2

Input

4 1 3 2

4

Output

0

Explanation

The city at index 0 is a perfect city because input1[0] and input1[1] are co-prime and input1[0] has a larger percentage of zombies than its neighboring city input1[1].

Input format
input1: An array representing the percentage of zombies in each city

input2: Number of cities in the country

Output format
Return the favorable city index 'i'.

'''


def zombies(a,n):
    l=[]
    for i in range(len(a)-1):
        c=0
        for j in range(2,min(a[i],a[i+1])+1):
            if a[i]%j==a[i+1]%j==0:
                c=1
        if c==0 and a[i]>a[i+1]:
            l.append(i)
    return l[0]
            
a=[int(x) for x in input().split()]
n=int(input())
print(zombies(a,n))