n,k=map(int,input().split())
nList = [i for i in range(n+1)]
defk = k
print("<",end="")
while len(nList)>2:
  if k%n == 0:
    print(nList.pop(n),end=", ")
    k = 1
  else:
    print(nList.pop(k),end=", ")
  n -= 1
  k = (k+defk-1)%n
print(str(nList[1])+">")