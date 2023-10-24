numlist = [0 for _ in range(10001)]
for i in range(10001):
  temp = 0
  for j in str(i):
    temp += int(j)
  if temp+i < 10001:
    numlist[temp+i] = 1
for i in range(1,10001):
  if numlist[i] == 0:
    print(i)
        