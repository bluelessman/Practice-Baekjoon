num = int(input())
plist = []
answer=0
for i in range(100):
    plist.append([])
    for j in range(100):
        plist[i].append(0)
for i in range(num):
    a, b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            plist[j][k]=1
for i in plist:
  answer += sum(i)
print(answer)
        