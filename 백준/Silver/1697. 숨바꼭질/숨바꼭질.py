import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visited = [0] * 100001
queue = deque([N])

while queue:
  a = queue.popleft()
  if a == K:
    print(visited[a])
    break
  for i in (a-1, a+1, a*2):
    if 0<=i<=100000 and not visited[i]:
      visited[i] = visited[a] + 1
      queue.append(i)