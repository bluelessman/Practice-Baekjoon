import sys
m,n=map(int,sys.stdin.readline().split())
p = [1,1]+[0]*(n-1)
for i in range(2,n+1):
    for j in range(i,n+1,i):
      if j!=i:
        p[j]=1
for i in range(m,len(p)):
    if p[i]==0:
        print(i)
        
        