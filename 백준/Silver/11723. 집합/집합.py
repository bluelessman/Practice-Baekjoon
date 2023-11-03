import sys
s = set()
N = int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "add":
      s.add(int(order[1]))
    elif order[0] == "remove":
      if int(order[1]) in s:
        s.remove(int(order[1]))
    elif order[0] == "check":
      if int(order[1]) in s:
        print(1)
      else:
        print(0)
    elif order[0] == "toggle":
      if int(order[1]) in s:
        s.remove(int(order[1]))
      else:
        s.add(int(order[1]))
    elif order[0] == "all":
      s = {j+1 for j in range(20)}
    elif order[0] == "empty":
      s = set()