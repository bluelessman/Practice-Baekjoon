from itertools import permutations
n,m=map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort()
ans = list(permutations(nlist,m))
for i in ans: 
  for j in i:
    print(j,end=" ")
  print()