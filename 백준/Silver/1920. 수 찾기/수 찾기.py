import sys

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] ==  target:
      return 1
    elif array[mid] > target:
      end = mid-1
    elif array[mid] < target:
      start = mid+1
  return 0

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

for i in X:
  print(binary_search(A, i, 0, len(A)-1))