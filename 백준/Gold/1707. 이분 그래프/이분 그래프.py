import sys
sys.setrecursionlimit(10**6)

def dfs(graph, start, color):
  visited[start] = color
  for i in graph[start]:
    if not visited[i]:
      result = dfs(graph, i, -color)
      if not result:
        return False
    elif visited[i] == color:
      return False
  return True
    

N = int(sys.stdin.readline())

for _ in range(N):
  V, E = map(int, sys.stdin.readline().split())
  graph = [[] for _ in range(V+1)]
  for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
  visited = [0] * (V+1)
  for i in range(1, V+1):
    if visited[i] == 0:
      result = dfs(graph, i, 1)
      if not result:
        break
  if result == True:
    print('YES')
  else:
    print('NO')