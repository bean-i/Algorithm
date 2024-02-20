import sys

def back():
  if len(lis) == M:
    print(*lis)
    return
  for x in range(1, N+1):
    lis.append(x)
    back()
    lis.pop()

N, M = map(int, sys.stdin.readline().split())

lis = []
back()