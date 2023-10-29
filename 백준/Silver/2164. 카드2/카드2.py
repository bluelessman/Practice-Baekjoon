from collections import deque
N = int(input())
queue = deque(i+1 for i in range(N))
if len(queue)==1:
    print(queue.pop())
while queue:
  queue.popleft()
  if len(queue)==1:
    print(queue.pop())
    break
  else:
    queue.append(queue.popleft())