import sys, heapq

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append([v, w])

start, end = map(int, sys.stdin.readline().split())

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

print(distance[end])