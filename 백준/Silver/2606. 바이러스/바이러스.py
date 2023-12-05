from collections import deque

def bfs(graph,v,visited):
    que = deque([v])
    ans = []
    visited[v] = True
    while que:
        x = que.popleft()
        ans.append(x)
        for i in graph[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = True;
    return ans
    
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
m = int(input())
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = bfs(graph,1,visited)
print(len(ans)-1)

