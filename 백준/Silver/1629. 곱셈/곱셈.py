import sys
a,b,c=map(int,sys.stdin.readline().split())
result = 1
duple = a
z = bin(b)
for i in range(-1,-len(z)+1,-1):
  if(z[i]=="1"):
    result = (result*duple)%c
  duple = (duple*duple)%c
print(result%c)