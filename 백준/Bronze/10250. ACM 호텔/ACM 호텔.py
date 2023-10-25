N = int(input())
for i in range(N):
    a,b,c=map(int,input().split())
    if c%a==0:
        print(a*100+c//a)
    else:
        print((c%a)*100+c//a+1)