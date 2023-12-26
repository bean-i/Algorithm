import sys

N, M = map(int, sys.stdin.readline().split())
tree = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = max(tree)

result = 0
while start <= end:
    L = 0
    mid = (start + end) // 2
    #자르고 난 후, 남는 길이 계산
    for i in tree:
      if i > mid:
        L += i - mid
    if L < M:
      end = mid - 1
    else:
      result = mid
      start = mid + 1

print(result)