import sys

N, M = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

#구간 합 구하기
sum = [0]
s = 0
for i in data:
  s += i
  sum.append(s)

for _ in range(M):
  left, right = map(int, sys.stdin.readline().split())
  print(sum[right] - sum[left-1])