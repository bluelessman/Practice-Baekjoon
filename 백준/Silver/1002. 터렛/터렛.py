t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    dis = (l[3]-l[0])**2 + (l[4]-l[1])**2
    if dis == 0 and l[2] == l[5]:
      print(-1)
    elif dis == (l[2]+l[5])**2 or dis == (abs(l[2]-l[5]))**2:
      print(1)
    elif dis < (l[2]+l[5])**2 and dis > (abs(l[2]-l[5]))**2:
      print(2)
    else:
      print(0)
    