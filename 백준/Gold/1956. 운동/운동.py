import sys
INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
graph = [[INF] * V for _ in range(V)]

for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u-1][v-1] = w

for i in range(V):
  graph[i][i] = 0

#플로이드워셜
for i in range(V):
  for a in range(V):
    for b in range(V):
      graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

result = []
#사이클 최단 경로 찾기
for a in range(V):
  for b in range(V):
    if graph[a][b] != 0 and graph[a][b] != INF and graph[b][a] != 0 and graph[b][a] != INF:
      result.append(graph[a][b] + graph[b][a])

if result:
  print(min(result))
else:
  print(-1)