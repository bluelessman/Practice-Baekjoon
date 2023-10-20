import sys
N = sys.stdin.readline()
numN = int(N)
answer = 0
nsum = 0
for i in range(max(0,numN-len(N)*9),numN):
    nsum = sum(map(int,str(i)))+i
    if nsum == numN:
        answer = i
        break
print(answer)