import sys

def back(start):
  if len(ans) == M:
    print(*ans)
    return
  for i in range(start, N+1):
    ans.append(i)
    back(i)
    ans.pop()

N, M = map(int, sys.stdin.readline().split())
ans = []
back(1)