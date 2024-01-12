import sys

def back(start):
  if len(ans) == M:
    print(*ans)
    return
  for i in range(start, N+1):
    if i not in ans:
      ans.append(i)
      back(i+1)
      ans.pop()

N, M = map(int, sys.stdin.readline().split())
ans = []
back(1)