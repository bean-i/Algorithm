import sys
from collections import deque

def bfs():
  while queue:
    x, y = queue.popleft()
    #오른쪽 이동
    if y+1 < M:
      if graph[x][y+1] == 1:
        graph[x][y+1] = graph[x][y]+1
        queue.append((x, y+1))
    #아래 이동
    if x+1 < N:
      if graph[x+1][y] == 1:
        graph[x+1][y] = graph[x][y]+1
        queue.append((x+1, y))
    #위 이동
    if x-1 >= 0:
      if graph[x-1][y] == 1:
        graph[x-1][y] = graph[x][y]+1
        queue.append((x-1, y))
    #왼쪽 이동
    if y-1 >= 0:
      if graph[x][y-1] == 1:
        graph[x][y-1] = graph[x][y]+1
        queue.append((x, y-1))

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

queue = deque()
queue.append([0, 0])
bfs()

print(graph[N-1][M-1])