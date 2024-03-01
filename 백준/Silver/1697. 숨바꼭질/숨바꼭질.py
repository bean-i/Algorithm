import sys
from collections import deque

def bfs(a):
  q = deque()
  q.append(a)
  while q:
    now = q.popleft()
    if now == K:
      return visited[now]
    for i in (now-1, now+1, 2*now):
      if 0<=i<=100000 and not visited[i]:
        visited[i] = visited[now] + 1
        q.append(i)


N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
print(bfs(N))