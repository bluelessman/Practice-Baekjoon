N = int(input())
for i in range(N):
  count = 0
  numlist = list(map(int,input().split()))
  avg = (sum(numlist)-numlist[0])/numlist[0]
  for j in range(1,len(numlist)):
    if numlist[j] > avg:
      count += 1
  print(f"{count*100/numlist[0]:0.3f}%")
