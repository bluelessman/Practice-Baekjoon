N = int(input())
ans = 0
for i in range(1,N+1):
  if i < 100:
    ans += 1
  else:
      sI = str(i)
      dif = int(sI[0])-int(sI[1])
      isTrue = True
      for j in range(2,len(sI)):
        if int(sI[j-1]) - int(sI[j]) != dif:
          isTrue = False
          break
      if isTrue:
        ans += 1
print(ans)