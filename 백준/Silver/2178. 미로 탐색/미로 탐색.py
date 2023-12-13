import sys
from collections import deque

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          queue.append([nx, ny])

N, M = map(int, sys.stdin.readline().split())
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(N):
  graph.append(list(map(int, input())))

queue = deque()
queue.append([0, 0])
bfs()

print(graph[N-1][M-1])