N = int(input())
nlist = [0 for _ in range(N+1)]
nlist[1] = 0
for i in range(2,N+1):
  nlist[i] = 1 + nlist[i-1]
  if i%2 == 0:
    nlist[i] = min(nlist[i],nlist[i//2]+1)
  if i%3 == 0:
    nlist[i] = min(nlist[i],nlist[i//3]+1)
print(nlist[N])