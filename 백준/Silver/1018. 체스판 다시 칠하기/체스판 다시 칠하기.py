N,M = map(int,input().split())
chess = []
ans = 100
for i in range(N):
    chess.append(input())
for i in range(N-7):
  for j in range(M-7):
    bFirst = 0
    wFirst = 0
    for k in range(i,i+8):
      for l in range(j,j+8):
        if (k+l-i-j)%2==0:
          if chess[k][l] == 'W':
            bFirst += 1
          else:
            wFirst += 1
        else:
          if chess[k][l] == 'W':
            wFirst += 1
          else:
            bFirst += 1
    cur = min(wFirst,bFirst)
    if cur < ans:
      ans = cur
print(ans)