import sys

def dfs(x, y):
  global cnt
  if x<=-1 or x>=N or y<=-1 or y>=N:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    cnt+=1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

graph = []
N = int(sys.stdin.readline())

for _ in range(N):
  graph.append(list(map(int, input())))

result = []
for i in range(N):
  for j in range(N):
    cnt=0
    if dfs(i, j) == True:
      result.append(cnt)

result.sort()
print(len(result))
for i in result:
  print(i)