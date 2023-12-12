import sys
from collections import deque

def bfs():
  while queue:
    x, y = queue.popleft()
    if x-1 >= 0:
      if graph[x-1][y] == 0:
        graph[x-1][y] = graph[x][y] + 1
        queue.append((x-1, y))
    if x+1 < N:
      if graph[x+1][y] == 0:
        graph[x+1][y] = graph[x][y] + 1
        queue.append((x+1, y))
    if y-1 >= 0:
      if graph[x][y-1] == 0:
        graph[x][y-1] = graph[x][y] + 1
        queue.append((x, y-1))
    if y+1 <M:
      if graph[x][y+1] == 0:
        graph[x][y+1] = graph[x][y] + 1
        queue.append((x, y+1))

M, N = map(int, sys.stdin.readline().split())
graph = []
day = 0
queue = deque()

for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      queue.append([i, j])

bfs()

for i in graph:
  for j in i:
    if j == 0:
      print(-1)
      exit()
  day = max(day, max(i))

print(day-1)