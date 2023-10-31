from collections import deque
import sys
import math
def cutting(i):
    i = math.floor(i*10)
    if i%10 < 5:
        i = i//10
    else:
        i = i//10+1
    return i

n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.read().split()))
nlist.sort()
ndeque = deque(nlist)
cut = cutting((n*15)/100)
for i in range(cut):
    ndeque.pop()
    ndeque.popleft()
if n == 0:
    print(0)
else:
    print(cutting(sum(ndeque)/len(ndeque)))