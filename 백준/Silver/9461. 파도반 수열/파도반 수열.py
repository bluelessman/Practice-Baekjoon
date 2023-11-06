ans = [0,1,1,1,2,2]
t = int(input())
for i in range(t):
  n = int(input())
  if n < len(ans):
    print(ans[n])
  else:
    while len(ans) !=n+1:
      ans.append(ans[-1]+ans[-5])
    print(ans[n])