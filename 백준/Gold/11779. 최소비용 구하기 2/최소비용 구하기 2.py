import sys, heapq

def dijkstra(start, end):
  distance = [INF] * (N+1)
  q=[]
  info = [0] * (N+1)
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for i in graph[node]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        info[i[0]] = node
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance[end], info

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append([v, w])

start, end = map(int, sys.stdin.readline().split())

a, b = dijkstra(start, end)

path = []
idx = end
while True:
  path.append(idx)
  if idx == start:
    break
  idx = b[idx]
  
path.reverse()
print(a)
print(len(path))
print(*path)