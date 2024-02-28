import sys
from collections import deque

def bfs():
  q = deque()
  q.append((0, 0, 1, 0)) # x, y, 거리, 벽을 부순 횟수
  visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 3차원 방문 배열
  visited[0][0][0] = 1 # 시작 위치 방문 표시
  
  while q:
    x, y, dist, wall = q.popleft()
    if x == N-1 and y == M-1:
      return dist
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M:
        #벽이 아닌 경우
        if graph[nx][ny] == 0 and visited[nx][ny][wall]==0:
          visited[nx][ny][wall] = 1
          q.append((nx, ny, dist + 1, wall))
          
        #벽인 경우
        if graph[nx][ny] == 1 and wall == 0 and visited[nx][ny][1]==0:
          visited[nx][ny][1] = 1
          q.append((nx, ny, dist + 1, 1))
  return -1


N, M = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

graph = []

for _ in range(N):
  a = list(map(int, sys.stdin.readline().rstrip()))
  graph.append(a)

print(bfs())