a = int(input())
if a == 1:
  print(1)
else:
  n = 1
  while (a - 1) > n * (n - 1) * 3:
    n += 1
  print(n)