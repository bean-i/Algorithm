import sys
from collections import deque

num = int(sys.stdin.readline())
queue = deque([i+1 for i in range(num)])

while len(queue)>1:
  queue.popleft()
  queue.append(queue.popleft())

print(queue[0])