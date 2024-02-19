import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

d = []
index = [-1] * N

#최대 길이 저장
for i in range(N):
  pos = bisect_left(d, A[i])
  if pos == len(d):
    d.append(A[i])
  else:
    d[pos] = A[i]
  index[i] = pos

#역추적
result = []
length = len(d) - 1
for i in range(N-1, -1, -1):
  if index[i] == length:
    length -= 1
    result.append(A[i])

result.reverse()
print(len(d))
print(*result)