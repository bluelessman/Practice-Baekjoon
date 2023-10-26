import sys
N = int(input())
ans = set(sys.stdin.read().split())
ans = sorted(ans)
ans = sorted(ans,key=len)
for i in ans:
    print(i)