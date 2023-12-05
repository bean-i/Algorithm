import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
  heapq.heappush(heap, int(sys.stdin.readline()))

result = 0
for i in range(len(heap)-1):
  add = 0
  add += heapq.heappop(heap)
  add += heapq.heappop(heap)
  result += add
  heapq.heappush(heap, add)

print(result)