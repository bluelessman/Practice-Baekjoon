from itertools import combinations_with_replacement

n,m= map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort()
ans = list(combinations_with_replacement(nlist,m))
for i in ans:
    for j in i:
        print(j,end=" ")
    print()