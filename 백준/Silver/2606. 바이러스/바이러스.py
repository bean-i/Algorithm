import sys
#DFS
def dfs(graph, r, visited):
  global cnt
  visited[r] = True
  for i in graph[r]:
    if not visited[i]:
      cnt+=1
      dfs(graph, i, visited)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

#그래프 초기화
graph = [[] for _ in range(N+1)]
cnt = 0
#그래프 입력 받기
for _ in range(M):
  n, m = map(int, sys.stdin.readline().split())
  graph[n].append(m)
  graph[m].append(n)

dfs(graph, 1, [False] * (N+1))
print(cnt)