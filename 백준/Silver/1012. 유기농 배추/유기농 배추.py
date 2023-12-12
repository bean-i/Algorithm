import sys
sys.setrecursionlimit(150000)
def dfs(x, y):
  if x<=-1 or x>=N or y<=-1 or y>=M:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

T = int(sys.stdin.readline())

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  graph = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    graph[y][x] = 1
  result = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j) == True:
        result+=1
  print(result)