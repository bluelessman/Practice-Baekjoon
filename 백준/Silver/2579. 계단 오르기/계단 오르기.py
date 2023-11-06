n = int(input())
ans = []
count = 0
prem = 0
for i in range(n):
  m = int(input())
  if i==0:
    ans.append(m)
  elif i==1:
    ans.append(ans[0]+m)
    count += 1
  elif i==2:
    ans.append(max(ans[0]+m,prem+m))
  else:
    ans.append(max(ans[i-2]+m,ans[i-3]+m+prem))
  prem = m
print(ans[n-1])