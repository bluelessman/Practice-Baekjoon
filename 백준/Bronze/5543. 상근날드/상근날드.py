import sys
nlist = list(map(int,sys.stdin.read().split()))
print(min(nlist[:3])+min(nlist[3:])-50)