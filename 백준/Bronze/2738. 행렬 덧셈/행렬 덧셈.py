N,M=map(int,input().split())
A = []
B = []
result = []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
for i in range(N):
  result.append([])
  for j in range(M):
    result[i].append(A[i][j]+B[i][j])
for i in range(N):
    for j in range(M):
        print(result[i][j], end=' ')
    print()
