import sys
n = int(sys.stdin.readline())
l = [0,1] + [0]*(n-1)
for i in range(2,n+1):
  k = int(i**0.5)
  mink = 10
  if k == i:
    l[i] = 1
  else:
    for j in range(1,k+1):
      if mink > 1+l[i-j**2]:
        mink = 1+l[i-j**2]
    l[i] = mink
print(l[n])