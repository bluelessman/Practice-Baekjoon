import heapq,sys
absheap = []
n = int(sys.stdin.readline())
for i in range(n):
  x = int(sys.stdin.readline())
  if x==0:
    if absheap:
      print(heapq.heappop(absheap)[1])
    else:
      print(0)
  else:
    heapq.heappush(absheap, (abs(x+0.1),x))