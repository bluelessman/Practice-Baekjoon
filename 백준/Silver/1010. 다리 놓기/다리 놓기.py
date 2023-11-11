l = [[0 for _ in range(31)]for _ in range(31)]
for i in range(1,31):
  l[1][i] = i

def b(n,m):
  if n > m:
    return 0
  if l[n][m] != 0:
    return l[n][m]
  else:
    for i in range(1,m):
      l[n][m] += b(n-1,m-i)
    return l[n][m]

t = int(input())
for i in range(t):
  n,m=map(int,input().split())
  print(b(n,m))