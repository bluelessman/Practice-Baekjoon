import heapq,sys
maxheap = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if maxheap:
            print(heapq.heappop(maxheap)[1])
        else:
            print(0)
    else:
        heapq.heappush(maxheap,(-x,x))