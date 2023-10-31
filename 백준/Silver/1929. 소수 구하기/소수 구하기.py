from math import floor
import sys
m,n=map(int,sys.stdin.readline().split())
if m == 1:
  m += 1
for i in range(m,n+1):
  isPrime = True
  for j in range(2,floor(i**0.5)+1):
    if i%j==0:
      isPrime = False
      break
  if isPrime:
    print(i)