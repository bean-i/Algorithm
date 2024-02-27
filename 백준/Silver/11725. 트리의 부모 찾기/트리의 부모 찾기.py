import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

result = [0] *(N+1)
visited = [False] * (N+1)
q = deque()
q.append(1)
visited[1] = True
while q:
  now = q.popleft()
  for i in graph[now]:
    if not visited[i]:
      visited[i] = True
      q.append(i)
      result[i] = now
      

for i in result[2:]:
  print(i)