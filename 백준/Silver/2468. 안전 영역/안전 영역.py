import sys
from collections import deque

def bfs(x, y, check, visited):
  q = deque()
  q.append((x, y))
  visited[x][y] = 1

  while q:
    a, b = q.popleft()
    for i in range(4):
      a1, b1 = a + dx[i], b + dy[i]
      if 0 <= a1 < N and 0 <= b1 < N:
        if graph[a1][b1] > check and visited[a1][b1] == 0:
          visited[a1][b1] = 1
          q.append((a1, b1))

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
#수위에 따른 안전영역 구하기
for i in range(max(map(max, graph))):
  visited = [[0]*N for _ in range(N)]
  cnt = 0
  for x1 in range(N):
    for y1 in range(N):
      if visited[x1][y1] == 0 and graph[x1][y1] > i:
        cnt += 1
        bfs(x1, y1, i, visited)
  result.append(cnt)

print(max(result))