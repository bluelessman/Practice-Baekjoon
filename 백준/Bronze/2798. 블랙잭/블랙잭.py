import sys
N,M = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
trisum = 0
maxsum = 0
for i in range(1,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            trisum = numlist[i] + numlist[j] + numlist[k]
            if trisum > maxsum and trisum <= M:
                maxsum = trisum
print(maxsum)