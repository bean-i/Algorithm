import sys
from collections import deque
#몇 덩어리인지 확인
def bfs(a, b):
  queue.append((a,b))
  while queue:
    x,y = queue.popleft()
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if ice[nx][ny] != 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            queue.append((nx,ny))
  return 1
  
#줄어드는 수 만큼 빙하 녹이기
def melted(bada):
  for i in range(N):
    for j in range(M):
      a = ice[i][j]-bada[i][j]
      if a < 0 :
        a=0
      ice[i][j] = a

#1년 후 줄어드는 수.
def melt():
  bada = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      cnt=0
      if ice[i][j] != 0:
        if ice[i-1][j] == 0: cnt+=1
        if ice[i+1][j] == 0: cnt+=1
        if ice[i][j-1] == 0: cnt+=1
        if ice[i][j+1] == 0: cnt+=1
        bada[i][j] = cnt
  melted(bada)
  
N, M = map(int, sys.stdin.readline().split())
ice = []
day=0
check=False
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
  ice.append(list(map(int, sys.stdin.readline().split())))

while True:
  visited = [[False]*M for _ in range(N)]
  result = 0
  for i in range(N):
    for j in range(M):
      if ice[i][j] != 0 and visited[i][j] == False:
        result += bfs(i,j)
  melt()
  if result == 0: # 빙산이 다없어질때까지 분리가 되지않으면 break
        break
  if result >= 2: # 빙산이 분리되면 break
    check = True
    break
  day += 1
  
if check:        
    print(day)
else:
    print(0)