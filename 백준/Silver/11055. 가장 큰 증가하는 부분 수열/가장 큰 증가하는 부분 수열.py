import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

d = A[:]

for i in range(N):
  for j in range(i):
    if A[j] < A[i]:
      d[i] = max(d[i], d[j]+A[i])
print(max(d))