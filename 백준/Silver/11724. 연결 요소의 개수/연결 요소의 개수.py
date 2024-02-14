import sys
from collections import deque

def bfs(start):
  q = deque([start])
  visited[start] = True
  while q:
    a = q.popleft()
    for i in graph[a]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (N+1)
cnt = 0
for i in range(1, N+1):
  if visited[i] == False:
    bfs(i)
    cnt+=1
print(cnt)