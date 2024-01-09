import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

#입력받기
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  indegree[b] += 1

#위상정렬
result = []
h = []
#진입차수 0인 노드 저장
for i in range(1, N+1):
  if indegree[i] == 0:
    heapq.heappush(h, i)
    
while h:
  now = heapq.heappop(h)
  result.append(now)
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(h, i)

print(*result)