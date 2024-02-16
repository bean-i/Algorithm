import sys

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
result = 0
edges = []
parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

for _ in range(M):
  a, b, cost = map(int, sys.stdin.readline().split())
  edges.append((cost, a, b))

edges.sort()
for i in edges:
  cost, a, b = i
  #사이클이 발생하지 않으면
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    

print(result)