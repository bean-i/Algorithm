import sys, copy
sys.setrecursionlimit(100000)
def dfs(graph1, x, y, check):
  if x <= -1 or y <= -1 or x >= N or y >= N:
    return False
  if graph1[x][y] > check:
    graph1[x][y] = 0
    dfs(graph1, x-1, y, check)
    dfs(graph1, x+1, y, check)
    dfs(graph1, x, y-1, check)
    dfs(graph1, x, y+1, check)
    return True
  return False

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

result = []
#수위에 따른 안전영역 구하기
for i in range(max(map(max, graph))):
  graph1 = copy.deepcopy(graph)
  cnt = 0
  for x1 in range(N):
    for y1 in range(N):
      if graph1[x1][y1] != 0 and graph1[x1][y1] > i:
        cnt += 1
        dfs(graph1, x1, y1, i)
  result.append(cnt)

print(max(result))