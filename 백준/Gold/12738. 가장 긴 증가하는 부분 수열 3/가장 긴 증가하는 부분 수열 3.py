import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

lis = []

for i in A:
  pos = bisect_left(lis, i)
  if pos == len(lis):
    lis.append(i)
  else:
    lis[pos] = i

print(len(lis))