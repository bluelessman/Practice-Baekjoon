n = int(input())
prev = [int(input())]
new = [];
for i in range(2,n+1):
  new = list(map(int,input().split()))
  for j in range(len(new)):
    if j==0:
      new[j] += prev[j]
    elif j==(len(new)-1):
      new[j] += prev[j-1]
    else:
      new[j] += max(prev[j],prev[j-1])
  prev = []
  for j in range(len(new)):
    prev.append(new[j])
if(n==1): print(prev[0])
else: print(max(new))