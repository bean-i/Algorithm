import sys

def back(i):
  if len(lis) == M:
    print(*lis)
    return
  for x in range(i+1, N+1):
    if x not in lis:
      lis.append(x)
      back(x)
      lis.pop()

N, M = map(int, sys.stdin.readline().split())

lis = []
back(0)