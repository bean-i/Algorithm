import sys

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

T = int(sys.stdin.readline())
for _ in range(T):
  N, M = map(int, sys.stdin.readline().split())
  parent = [0] * (N+1)
  edges = []
  result = 0
  #부모 테이블 초기화
  for i in range(1, N+1):
    parent[i] = i
  for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))
  for edge in edges:
    a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
      result += 1
      union_parent(parent, a, b)
  print(result)