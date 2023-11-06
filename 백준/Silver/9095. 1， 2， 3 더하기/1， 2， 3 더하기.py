ans = [0,1,2,4]
t = int(input())
for i in range(t):
  n = int(input())
  if n < len(ans):
    print(ans[n])
  else:
    while len(ans) != n+1:
      ans.append(ans[len(ans)-3]+ans[len(ans)-2]+ans[len(ans)-1])
    print(ans[n])