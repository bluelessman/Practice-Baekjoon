import sys
n,m=map(int,input().split())
numlist = list(range(0,n+1))
temp = 0
for i in range(m):
    count = 0
    a,b=map(int,sys.stdin.readline().split())
    middle = ((a+b)//2)+1
    for j in range(a,middle):
        temp =numlist[j]
        numlist[j]=numlist[b-count]
        numlist[b-count]=temp
        count += 1
for i in range(n):
    print(numlist[i+1],end=" ")