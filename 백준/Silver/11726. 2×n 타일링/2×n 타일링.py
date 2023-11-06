import sys
n = int(sys.stdin.readline())
l = [0,1,2]+[0]*(n-2)
for i in range(3,n+1):
    l[i] = l[i-2]+l[i-1]
print(l[n]%10007)