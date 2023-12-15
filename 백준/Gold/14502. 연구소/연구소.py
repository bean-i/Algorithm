import sys
import copy
from collections import deque

def bfs():
  queue1 = copy.deepcopy(queue)
  while queue1:
    x, y = queue1.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if graph1[nx][ny] == 0:
          graph1[nx][ny] = 2
          queue1.append([nx, ny])
  cnt = 0
  for i in range(N):
    for j in range(M):
      if graph1[i][j] == 0:
        cnt+=1
  return cnt
  
  
#그래프 입력받기
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
#벽 세울 수 있는 좌표 모음
list0 = []

#초기 그래프에서 바이러스가 있는 좌표 모음
queue = deque()

#벽 세울 수 있는 곳의 좌표 탐색
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      list0.append((i, j))
#바이러스가 있는 곳 탐색
for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      queue.append((i, j))

result = []
for i in range(0, len(list0)-2):
  for j in range(i+1, len(list0)-1):
    for k in range(j+1, len(list0)):
      graph1 = copy.deepcopy(graph)
      graph1[list0[i][0]][list0[i][1]] = 1
      graph1[list0[j][0]][list0[j][1]] = 1
      graph1[list0[k][0]][list0[k][1]] = 1
      result.append(bfs())

print(max(result))
