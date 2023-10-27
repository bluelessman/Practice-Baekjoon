import sys
N = int(sys.stdin.readline())
l = []
for i in range(N):
    l.append(sys.stdin.readline().split())
l.sort(key=lambda age: int(age[0]))
for i in l:
    print(i[0],i[1])