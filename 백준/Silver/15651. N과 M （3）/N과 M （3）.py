from itertools import product
n,m=map(int,input().split())
nlist = [i+1 for i in range(n)]
mlist = list(product(nlist,repeat = m))
for i in mlist:
  for j in i:
    print(j, end=" ")
  print()