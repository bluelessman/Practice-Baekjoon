from itertools import permutations
n,m=map(int,input().split())
nlist = list(map(int,input().split()))
ans = list(set(permutations(nlist,m)))
for i in sorted(ans):
  for j in i:
    print(j,end=" ")
  print()