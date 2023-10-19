M = int(input())
N = int(input())
numlist = []
minD = 0
isMin = True
for i in range(M,N+1):
    if i == 1:
      continue
    rooti = int(i**0.5)
    isDecimal = True
    for j in range(2,rooti+1):
        if i%j == 0:
            isDecimal = False
            break
    if isDecimal:
        numlist.append(i)
        if isMin:
            isMin = False
            minD = i
if isMin:
  print(-1)
else:
  print(sum(numlist))
  print(minD)
