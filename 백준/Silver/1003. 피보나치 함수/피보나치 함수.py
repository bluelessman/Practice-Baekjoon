import sys
flist = [[1,0],[0,1]]
n = int(sys.stdin.readline())
for i in range(n):
  k = int(sys.stdin.readline())
  for j in range(len(flist),k+1):
    flist.append([flist[j-1][0]+flist[j-2][0],flist[j-1][1]+flist[j-2][1]])
  print(flist[k][0],flist[k][1])