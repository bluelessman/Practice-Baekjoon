import sys
num , typ = sys.stdin.readline().split()
a = 0
typ = int(typ)
l = len(num)
for i in num:
  if i.isdigit() :
    a += int(i)*(typ**(l-1))
  else:
    a += (ord(i)-55)*(typ**(l-1))
  l -= 1
print(a)