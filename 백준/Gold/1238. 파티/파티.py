import sys, heapq

def dijkstra(start, end):
  distance = [INF] * (N+1)
  q=[]
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for i in graph[node]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return distance[end]

INF = int(1e9)

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append([v, w])

result = []
for i in range(1, N+1):
  result.append(dijkstra(i, X) + dijkstra(X, i))

print(max(result))