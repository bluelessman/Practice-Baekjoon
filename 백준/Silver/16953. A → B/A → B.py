n,m=map(int,input().split())
count = 1
while(m>n):
  count+= 1
  if(m%10==1):
    m //= 10
  elif(m%2==0):
    m //= 2
  else:
    break
if(m==n):
  print(count)
else:
  print(-1)