import sys
from collections import deque

def dfs(start, visited):
  visited[start] = True
  print(start, end=' ')
  for i in graph[start]:
    if not visited[i]:
      dfs(i, visited)

def bfs(start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N+1):
  graph[i].sort()

dfs(V, [False] * (N+1))
print()
bfs(V, [False] * (N+1))