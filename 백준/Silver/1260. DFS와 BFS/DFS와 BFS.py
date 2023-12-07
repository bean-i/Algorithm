import sys
from collections import deque
#BFS
def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    a = queue.popleft()
    print(a, end=' ')
    for i in graph[a]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
#DFS
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

#그래프 입력받기
for i in range(M):
  n, m = map(int, sys.stdin.readline().split())
  graph[n].append(m)
  graph[m].append(n)

#정렬
for i in range(N+1):
  graph[i].sort()

dfs(graph, V, [False]*(N+1))
print()
bfs(graph, V, [False]*(N+1))