from itertools import permutations
n,m=map(int,input().split())
nlist = [i+1 for i in range(n)]
mlist = list(permutations(nlist,m))
for i in mlist:
  for j in i:
    print(j, end=" ")
  print()