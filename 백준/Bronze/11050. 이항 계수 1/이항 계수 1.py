import math
N,K=map(int,input().split())
fac = math.factorial
print(fac(N)//(fac(N-K)*fac(K)))