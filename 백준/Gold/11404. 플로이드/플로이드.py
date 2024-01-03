import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  if graph[a][b] != INF and c > graph[a][b]:
    continue
  graph[a][b] = c
  
for k in range(n+1):
  for i in range(n+1):
    for j in range(n+1):
      if i == j:
        graph[i][j] = 0
      else:
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()