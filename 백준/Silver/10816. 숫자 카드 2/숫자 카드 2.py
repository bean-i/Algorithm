import sys
from bisect import bisect_left, bisect_right

def count(array, target):
  left_index = bisect_left(array, target)
  right_index = bisect_right(array, target)
  return right_index - left_index

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

for i in X:
  print(count(A, i), end=' ')