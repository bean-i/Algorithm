import sys
from collections import deque

def bfs():
  q = deque()
  q.append((0, 0))

  while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
      return graph[x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M:
        if graph[nx][ny] == 1:
          q.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1

N, M = map(int, sys.stdin.readline().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs())