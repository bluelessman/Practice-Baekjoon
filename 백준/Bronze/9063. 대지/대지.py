import sys
N = int(sys.stdin.readline())
maxX,minX,maxY,minY=-1000000,1000000,-1000000,1000000
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    if x > maxX:
        maxX=x
    if x < minX:
        minX=x
    if y > maxY:
        maxY=y
    if y < minY:
        minY=y
answer = (maxX-minX)*(maxY-minY)
print(answer)

    