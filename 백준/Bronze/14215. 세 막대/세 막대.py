nlist=list(map(int,input().split()))
if sum(nlist)-max(nlist) > max(nlist):
    print(sum(nlist))
else:
    print((sum(nlist)-max(nlist))*2-1)