import sys
n,m = map(int,sys.stdin.readline().split())
dic = dict()
ans = []
for i in range(n):
    order = sys.stdin.readline().rstrip()
    dic[order]=1
for i in range(m):
    order = sys.stdin.readline().rstrip()
    if order in dic:
        ans.append(order)
ans = sorted(ans)
print(len(ans))
for i in ans:
    print(i)