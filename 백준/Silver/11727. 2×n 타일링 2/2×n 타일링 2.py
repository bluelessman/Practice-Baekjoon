n = int(input())
l = [0,1,3]+[0]*(n-2)
for i in range(3,n+1):
    l[i]=l[i-1]+2*l[i-2]
print(l[n]%10007)