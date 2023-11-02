import sys
n,k=map(int,sys.stdin.readline().split())
nlist = list(map(int,sys.stdin.read().split()))
ans = 0
for i in nlist[::-1]:
    ans += k//i
    k = k%i
    if k==0:
        break
print(ans)