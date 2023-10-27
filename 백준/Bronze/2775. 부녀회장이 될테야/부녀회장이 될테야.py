f = [[0]*15 for _ in range(15)]
for i in range(1,15):
  f[0][i] = i
def fam(k,n):
  if f[k][n]!=0:
    return f[k][n]
  else:
    for i in range(1,n+1):
      f[k][n] += fam(k-1,i)
    return f[k][n]

T=int(input())
for i in range(T):
  k = int(input())
  n = int(input())
  print(fam(k,n))