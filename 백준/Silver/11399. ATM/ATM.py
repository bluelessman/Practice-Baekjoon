N = int(input())
P = list(map(int,input().split()))
P.sort(reverse=True)
ans = 0
for i in range(N):
  for j in range(i,N):
    ans += P[j]
print(ans)