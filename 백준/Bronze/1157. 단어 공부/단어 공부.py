a = input()
a = a.upper()
M = 0
isBoth = False
dic = {}
for i in a:
  if i in dic:
    dic[i] += 1
  else :
    dic[i] = 1
  if dic[i] > M:
    M = dic[i]
    Ma = i
    isBoth = False
  elif dic[i] == M:
    isBoth = True
if isBoth:
  print("?")
else:
  print(Ma)