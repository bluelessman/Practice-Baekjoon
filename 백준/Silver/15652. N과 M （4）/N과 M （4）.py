from itertools import combinations_with_replacement
n,m=map(int,input().split())
nlist = [i+1 for i in range(n)]
mlist = list(combinations_with_replacement(nlist,m))
for i in mlist:
  for j in i:
    print(j, end=" ")
  print()