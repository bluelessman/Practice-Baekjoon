import sys
n,m = map(int,input().split())
numlist = list(range(1,n+1))
temp = 0
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    temp = numlist[a-1]
    numlist[a-1]=numlist[b-1]
    numlist[b-1]=temp
for i in range(n):
    print(numlist[i])
    