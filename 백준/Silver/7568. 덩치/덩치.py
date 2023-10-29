n = int(input())
l = []
ans = [1 for _ in range(n)]
for i in range(n):
  l.append(list(map(int,input().split())))
for i in range(n):
  for j in range(n):
    if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
      ans[i] += 1
for i in ans:
  print(i,end=' ')