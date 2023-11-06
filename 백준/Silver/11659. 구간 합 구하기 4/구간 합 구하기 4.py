import sys
n,m = map(int,sys.stdin.readline().split())
nlist = [0]+list(map(int,sys.stdin.readline().split()))
for i in range(1,n+1):
    nlist[i] = nlist[i] + nlist[i-1]
for x in range(m):
    i,j = map(int,sys.stdin.readline().split())
    print(nlist[j]-nlist[i-1])