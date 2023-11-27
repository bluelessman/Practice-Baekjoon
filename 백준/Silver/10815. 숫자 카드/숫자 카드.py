import sys
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))
d = dict()
for i in nlist:
    d[i] = 1;
m = int(sys.stdin.readline())
mlist = list(map(int,sys.stdin.readline().split()))
for i in mlist:
    if d.get(i)==None:
        print(0,end=" ")
    else:
        print(1,end=" ")