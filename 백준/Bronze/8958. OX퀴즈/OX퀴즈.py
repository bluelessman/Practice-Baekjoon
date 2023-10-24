N = int(input())
for i in range(N):
  str = input()
  count = 0
  ans = 0
  for j in str:
    if j == 'O':
      count += 1
      ans += count
    else:
      count = 0
  print(ans)