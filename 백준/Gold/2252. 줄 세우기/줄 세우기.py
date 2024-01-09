import sys
from collections import deque

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
q = deque()
#진입차수 0인 노드 저장
for i in range(1, N+1):
  if indegree[i] == 0:
    q.append(i)
while q:
  now = q.popleft()
  result.append(now)
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      q.append(i)


print(*result)