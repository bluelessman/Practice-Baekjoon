numlist = []
for i in range(10001):
  temp = 0
  for j in str(i):
    temp += int(j)
  numlist.append(temp+i)
for i in range(10001):
  if i not in numlist:
    print(i)
        