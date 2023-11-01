from math import floor
def cutting(i):
  i = floor(i*10)
  if i%10 < 5:
    i = i//10
  else:
    i = i//10+1
  return i
N = int(input())
nsum = 0
nlist = []
ndic = {}
nmax = 0
nmaxlist = []
for i in range(N):
  n = int(input())
  nsum += n
  nlist.append(n)
  if n in ndic:
    ndic[n]+=1
  else:
    ndic[n]=1
  if ndic[n]>nmax:
    nmax = ndic[n]
    nmaxlist = [n]
  elif ndic[n]==nmax:
    nmaxlist.append(n)
nlist.sort()
nsum = cutting(nsum/N)
print(nsum)
ncen = nlist[N//2]
print(ncen)
if len(nmaxlist)==1:
  print(nmaxlist[0])
else:
  nmaxlist.sort()
  print(nmaxlist[1])
nbo = nlist[-1]-nlist[0]
print(nbo)