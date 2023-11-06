t = int(input())
for i in range(t):
  n = int(input())
  if n==0:
    print(0)
    continue
  ans = 1
  dic = dict()
  for j in range(n):
    name, cloth = input().split()
    if cloth in dic:
      dic[cloth] += 1
    else:
      dic[cloth] = 1
  for cloth in dic:
    ans *= dic[cloth]+1
  print(ans-1)