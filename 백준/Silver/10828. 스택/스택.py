import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
  order = sys.stdin.readline().rstrip()
  if order[-1].isdigit():
    order = order.split()
    stack.append(order[1])
  elif order == 'top':
    if not stack:
      print(-1)
    else:
      print(stack[-1])
  elif order == 'size':
      print(len(stack))
  elif order == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  else:
    if not stack:
      print(-1)
    else:
      print(stack.pop())