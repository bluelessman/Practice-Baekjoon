import sys
n = int(sys.stdin.readline())
nl = list(map(int,sys.stdin.readline().split()))
nd = {}
for i in nl:
    nd[i] = 1
m = int(sys.stdin.readline())
ml = list(map(int,sys.stdin.readline().split()))
for i in ml:
    if i in nd:
        print(1)
    else:
        print(0)
        