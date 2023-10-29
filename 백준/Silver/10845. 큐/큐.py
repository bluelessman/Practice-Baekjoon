import sys
N = int(sys.stdin.readline())
queue=[]
for i in range(N):
    order = sys.stdin.readline().rstrip()
    if order[-1].isdigit():
        order, n = order.split()
        queue.append(int(n))
    elif order=='size':
        print(len(queue))
    elif order=='empty':
        if queue:
            print(0)
        else:
            print(1)
    else:
        if not queue:
            print(-1)
        elif order=='pop':
            print(queue.pop(0))
        elif order=='front':
            print(queue[0])
        else:
            print(queue[-1])