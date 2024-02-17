import sys

N, M = map(int, sys.stdin.readline().split())

tree  = list(map(int, sys.stdin.readline().split()))
tree.sort()

start = 0
end = max(tree)
result = 0

while start <= end:
  mid = (start + end) // 2
  cnt = 0
  for i in tree:
    if i > mid:
      cnt += i - mid
  if cnt < M:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
print(result)