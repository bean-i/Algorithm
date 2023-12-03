import sys
from collections import deque

num = int(sys.stdin.readline())
queue = deque([i+1 for i in range(num)])

i = 0
while True:
  if len(queue) == 1:
    break
  if i%2 == 0:
    queue.popleft()
  else:
    queue.append(queue[0])
    queue.popleft()
  i+=1

print(queue[0])