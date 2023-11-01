import sys
N = int(input())
NList = list(map(int,sys.stdin.read().split()))
s1 = []
s2 = [N-i for i in range(N)]
ans = []
count = 0
isTrue = True
for i in NList:
  count += 1
  if i > s2[-1]:
    while i != s2[-1]:
      s1.append(s2.pop())
      ans.append('+')
    s2.pop()
    ans.append('+')
    ans.append('-')
  elif i == s2[-1]:
    s2.pop()
    ans.append('+')
    ans.append('-')
  else:
    if s1[-1] == i:
      s1.pop()
      ans.append('-')
    else:
      isTrue = False
      break
  if not s2:
    break
for i in range(count,N):
  if s1[-1] == NList[i]:
    s1.pop()
    ans.append('-')
  else:
    isTrue = False
    break
if isTrue:
  while s1:
    s1.pop()
    ans.append('-')
  for i in ans:
    print(i)
else:
  print('NO')