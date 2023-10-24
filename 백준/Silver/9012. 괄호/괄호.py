N = int(input())
for i in range(N):
  count = 0
  isEnd = False
  ps = input()
  for j in ps:
    if j == ")":
      if count == 0:
        print("NO")
        isEnd = True
        break
      else :
        count -= 1
    else:
      count += 1
  if not isEnd:
    if count == 0:
      print("YES")
    else:
      print("NO")