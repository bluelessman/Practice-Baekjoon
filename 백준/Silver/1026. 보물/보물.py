n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
for i in range(n):
    count = 0
    for j in range(n):
        if (b[i]==b[j] and j>i) or b[i]>b[j]:
            count+=1
    ans += b[i]*a[count]
print(ans)