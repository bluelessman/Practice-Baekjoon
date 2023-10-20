import sys
N = sys.stdin.readline()
l = len(N)
N = int(N)

isexist = False
for i in range(N):
    nsum = i
    j = i
    while j != 0:
        nsum += j%10
        j = j//10
    if nsum == N:
        print(i)
        isexist = True
        break
if not isexist:
    print(0)