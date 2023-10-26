import math,sys
K,N = map(int,sys.stdin.readline().split())
nList = list(map(int,sys.stdin.read().split()))
right = sum(nList)//N
left = max(min(nList)//math.ceil(N/K),1)
while left<=right:
  n = 0
  ans = (right+left)//2
  for i in nList:
    n += i//ans
  if n >= N:
    left = ans+1
  else:
    right = ans-1
print(right)