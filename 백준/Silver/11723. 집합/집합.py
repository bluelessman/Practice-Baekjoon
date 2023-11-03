import sys
s = {i:0 for i in range(21)}
N = int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "add":
      s[int(order[1])] = 1
    elif order[0] == "remove":
      s[int(order[1])] = 0
    elif order[0] == "check":
      print(s[int(order[1])])
    elif order[0] == "toggle":
      if s[int(order[1])] == 0:
        s[int(order[1])]=1
      else:
        s[int(order[1])]=0
    elif order[0] == "all":
      for i in range(21):
        s[i] = 1
    elif order[0] == "empty":
      for i in range(21):
        s[i] = 0