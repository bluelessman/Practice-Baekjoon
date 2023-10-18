M,row,column=-1,0,0
for i in range(9):
    a = list(map(int, input().split()))
    if max(a)>M:
        M = max(a)
        row = i+1
        column = a.index(M)+1
print(M)
print(row,column)
        