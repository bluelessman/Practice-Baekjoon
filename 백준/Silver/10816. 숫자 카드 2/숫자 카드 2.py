import sys
n = int(sys.stdin.readline())
nl = list(map(int,sys.stdin.readline().split()))
nd = {}
for i in nl:
  if i in nd:
    nd[i] += 1
  else:
    nd[i] = 1
m = int(sys.stdin.readline())
ml = list(map(int,sys.stdin.readline().split()))
for i in ml:
  if i in nd:
    print(nd[i],end=' ')
  else:
    print(0,end=' ')