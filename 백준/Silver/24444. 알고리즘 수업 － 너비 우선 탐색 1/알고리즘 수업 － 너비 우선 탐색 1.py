import sys
from collections import deque
sys.setrecursionlimit(150000)
#BFS
def bfs(graph, r, visited):
  global cnt
  visited[r] = cnt
  queue = deque([r])
  while queue:
    a = queue.popleft()
    for i in graph[a]:
      if visited[i] == 0:
        cnt+=1
        queue.append(i)
        visited[i] = cnt
    
  for i in graph[r]:
    if visited[i] == 0:
      cnt+=1
      dfs(graph, i, visited)

N, M, R = map(int, sys.stdin.readline().split())
cnt = 1
#그래프 초기화
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
#그래프 입력 받기
for _ in range(M):
  n, m = map(int, sys.stdin.readline().split())
  graph[n].append(m)
  graph[m].append(n)
#오름차순 정렬
for i in range(N+1):
  graph[i].sort()

bfs(graph, R, visited)
for i in range(1, N+1):
  print(visited[i])