num, typ = map(int, input().split())
numlist = []
while num != 0:
    numlist.append(num%typ)
    num = num//typ

count = 0
for i in reversed(numlist):
  if i >= 10:
    print(chr(i+55),end="")
  else:
    print(i,end="")
    