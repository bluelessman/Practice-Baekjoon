t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    x, y = max(a,b),min(a,b)
    while x%y != 0:
        x, y = y, x%y
    print(a*b//y)