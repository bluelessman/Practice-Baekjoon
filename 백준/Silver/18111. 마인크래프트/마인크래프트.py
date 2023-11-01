import sys
h = dict()
for i in range(257):
  h[i] = 0
n,m,b=map(int,sys.stdin.readline().split())
maxh = -1
minh = 257
nlist = list(map(int,sys.stdin.read().split()))
ans = 512*len(nlist)
ansh = 0
for i in nlist:
  h[i] += 1
  if i > maxh:
    maxh = i
  if i < minh:
    minh = i
for i in range(minh,maxh+1):
  block = b
  temp = 0
  for j in range(minh,maxh+1):
    if j<i:
      temp += (i-j)*h[j]
      block -= (i-j)*h[j]
    else:
      temp += 2*(j-i)*h[j]
      block += (j-i)*h[j]
  if block >= 0 and temp <= ans:
    ans = temp
    ansh = i
print(ans,ansh)