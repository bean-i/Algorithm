import sys

N = int(sys.stdin.readline())
tps = [[0, 0] for _ in range(N+1)]

for i in range(1, N+1):
  t, p = map(int, sys.stdin.readline().split())
  tps[i][0], tps[i][1] = t, p


d = [0] * (N+2)
#i번째 일수를 맨 처음에 하는 경우
for i in range(1, N+1):
  d[i] = max(d[i], d[i-1])
  if i + tps[i][0] > N + 1:
    continue
  d[i+tps[i][0]] = max(d[i+tps[i][0]], d[i] + tps[i][1])

print(max(d))