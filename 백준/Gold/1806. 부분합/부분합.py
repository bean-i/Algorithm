import sys
from collections import deque

N, S = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

result = deque()
sum = 0
end = 0
count = 100001

for start in range(N):
  if sum < S:
    while sum < S and end < N:
      sum += data[end]
      result.append(data[end])
      end += 1
  if sum >= S:
    if len(result) < count:
      count = len(result)
  sum -= data[start]
  result.popleft()

if count == 100001:
  print(0)
else:
  print(count)