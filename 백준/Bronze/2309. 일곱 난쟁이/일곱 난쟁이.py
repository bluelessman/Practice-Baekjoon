import sys
h = list(map(int,sys.stdin.read().split()))
total = sum(h)
isEnd = False
for i in range(9):
    for j in range(i+1,9):
        if total - h[i] - h[j] == 100:
            a,b= h[i],h[j]
            h.remove(a)
            h.remove(b)
            isEnd = True
            break
    if isEnd:
      break
for i in sorted(h):
  print(i)