import sys, heapq
INF = int(1e9)

def dijkstra(graph, start, distance):
  road = [0] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    p_c, node = heapq.heappop(q)
    if distance[node] < p_c :
      continue
    for i in graph[node]:
      cost = p_c + i[1]
      if cost < distance[i[0]]:
        road[i[0]] = node
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  result = [0] * (n+1)
  for i in range(1, n+1):
    if i == start:
      result[i] = '-'
      continue
    now = i
    while True:
      if road[now] == start:
        break
      now = road[now]
    result[i] = now

  return result

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

#그래프 입력받기
for _ in range(m):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append((v, w))
  graph[v].append((u, w))

for i in range(1, n+1):
  answer = dijkstra(graph, i, [INF] * (n+1))
  print(*answer[1:])