import sys
N = int(sys.stdin.readline())
deque=[]
for i in range(N):
    order = sys.stdin.readline().rstrip()
    if order[-1].isdigit():
        order, n = order.split()
        if order == 'push_front':
            deque.insert(0,int(n))
        else:
            deque.append(int(n))
    elif order=='size':
        print(len(deque))
    elif order=='empty':
        if deque:
            print(0)
        else:
            print(1)
    else:
        if not deque:
            print(-1)
        elif order=='pop_back':
            print(deque.pop())
        elif order=='pop_front':
            print(deque.pop(0))
        elif order=='front':
            print(deque[0])
        else:
            print(deque[-1])