import sys

N, M = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

count = 0
sum = 0
end = 0

for start in range(N):
  while sum < M and end < N:
    sum += data[end]
    end += 1
  if sum == M:
    count += 1
  sum -= data[start]

print(count)