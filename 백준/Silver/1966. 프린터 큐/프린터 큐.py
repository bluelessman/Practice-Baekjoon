from collections import deque
N = int(input())
queue = deque([])
for i in range(N):
  n,m = map(int,input().split())
  l = deque(list(map(lambda x:[int(x),0],input().split())))
  l[m][1] = 1
  lmax = max(l,key=lambda x:x[0])
  count = 0
  while True:
    temp = l.popleft()
    if temp[0]!=lmax[0]:
      l.append(temp)
    else:
      count += 1
      if temp[1]==1:
        print(count)
        break
      else:
        lmax = max(l,key=lambda x:x[0])