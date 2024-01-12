import sys

def back():
  if len(ans) == M:
    print(*ans)
    return
  for i in range(1, N+1):
    if i not in ans:
      ans.append(i)
      back()
      ans.pop()

N, M = map(int, sys.stdin.readline().split())
ans = []

back()