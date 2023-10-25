N = list(map(int,input().split()))
isDesc = True
isAsc = True
for i in range(7):
    if N[i]-N[i+1] != 1:
        isDesc = False
    if N[i]-N[i+1] != -1:
        isAsc = False
if isDesc:
    print("descending")
elif isAsc:
    print("ascending")
else:
    print("mixed")
    