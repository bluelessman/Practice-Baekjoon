from collections import deque

def dfs(graph,v,visited):
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

def bfs(graph,v,visited):
  que = deque([v])
  visited[v] = True
  while que:
    x = que.popleft()
    print(x, end=" ")
    for i in graph[x]:
      if not visited[i]:
        que.append(i)
      visited[i] = True



n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
dv = [False] * (n+1)
bv = [False] * (n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
  i.sort()
dfs(graph,v,dv)
print()
bfs(graph,v,bv)