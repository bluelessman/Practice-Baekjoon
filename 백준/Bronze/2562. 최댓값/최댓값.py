a = []
maxvalue = 0
maxn = 0
for i in range(9):
    n = int(input())
    a.append(n)
    if maxvalue < n:
        maxvalue = n
        maxn = i+1
print(maxvalue)
print(maxn)