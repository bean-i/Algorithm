import sys
from collections import deque

case = int(sys.stdin.readline())

for _ in range(case):
  N, M = map(int, sys.stdin.readline().split())
  imp = deque(enumerate(list(map(int, sys.stdin.readline().split()))))
  num = imp[M]
  cnt = 0
  while True:
    m = max(imp, key = lambda x:x[1])
    if imp[0] == m:
      cnt+=1
      if imp[0] == num:
        break
      else:
        imp.popleft()
    else:
      imp.append(imp.popleft())
  print(cnt)