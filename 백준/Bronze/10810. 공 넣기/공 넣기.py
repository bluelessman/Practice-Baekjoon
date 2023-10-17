import sys
n,m=map(int,input().split())
numlist = [0 for i in range(n)]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    for k in range(a-1,b): 
        numlist[k]=c
for i in range(n):
    print(numlist[i])