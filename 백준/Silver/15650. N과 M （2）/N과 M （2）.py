import sys

def back():
  if len(ans) == M:
    print(*ans)
    return
  for i in range(1, N+1):
    if len(ans) == 0:
      ans.append(i)
      back()
      ans.pop()
    elif i not in ans and i > ans[-1]:
      ans.append(i)
      back()
      ans.pop()

N, M = map(int, sys.stdin.readline().split())
ans = []
back()