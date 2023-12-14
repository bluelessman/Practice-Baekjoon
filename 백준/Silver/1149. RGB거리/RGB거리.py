n = int(input())
rmin=gmin=bmin=0
for i in range(n):
  r,g,b = map(int,input().split())
  rmin,gmin,bmin = min(gmin,bmin)+r,min(rmin,bmin)+g,min(gmin,rmin)+b
print(min(rmin,min(gmin,bmin)))