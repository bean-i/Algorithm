import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, N+1)])
i = 0
result = []

while queue:
  if i+K-1 <= len(queue)-1:
    i+=K-1
    result.append(queue[i])
    del queue[i]
  else:
    i = (i+K-1)%len(queue)
    result.append(queue[i])
    del queue[i]

print('<', end='')
for i in range(len(result)):
  if i == len(result)-1:
    print(result[i], end='')
  else:
    print(result[i], end=', ')
print('>')