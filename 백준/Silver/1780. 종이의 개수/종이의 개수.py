import sys, heapq

def cut(x, y, z):
  c = graph[x][y]
  for i in range(x, x+z):
    for j in range(y, y+z):
      if graph[i][j] != c:
        for k in range(3):
          for l in range(3):
            cut(x + k * (z//3), y + l * (z//3), z//3)
        return
  if c == -1:
    ans[0] += 1
  elif c == 0:
    ans[1] += 1
  else:
    ans[2] += 1
      
N = int(sys.stdin.readline())
graph = []
for i in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))
ans = [0, 0, 0]
cut(0, 0, N)

print(*ans, sep='\n')