n,m=map(int,input().split())
big = max(n,m)
small = min(n,m)
while big%small != 0:
  temp = big%small
  big = small
  small = temp
print(small)
print(n*m//small)