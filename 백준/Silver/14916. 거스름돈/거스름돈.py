n = int(input())
init = 100001
l = [0]+[init]*n
for i in [2,5]:
    for j in range(i,n+1):
        if l[j-i] != init:
            l[j] = min(l[j],l[j-i]+1)
if l[n] == init:
    print(-1)
else:
    print(l[n])