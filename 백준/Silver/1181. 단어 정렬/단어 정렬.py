N = int(input())
ans = set()
for i in range(N):
    ans.add(input())
ans = sorted(ans)
ans = sorted(ans,key=len)
for i in ans:
    print(i)