import sys, heapq

INF = int(1e9)
#정점 V, 간선 E
V, E = map(int, sys.stdin.readline().split())
#시작 노드 K
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
  #출발, 도착, 가중치
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append((v, w))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    #방문한 경우 넘어감.
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
  if distance[i]==INF:
    print('INF')
  else:
    print(distance[i])