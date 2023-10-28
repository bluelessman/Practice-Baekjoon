import sys
N = int(sys.stdin.readline())
Nlist = []
for i in range(N):
    Nlist.append(list(map(int,sys.stdin.readline().split())))
Nlist.sort(key=lambda a:a[1])
Nlist.sort(key=lambda a:a[0])
for i in Nlist:
    print(i[0],i[1])