import sys

N, K = map(int, sys.stdin.readline().split())
t = [[0, 0]]
#입력 받기
for i in range(N):
  t.append(list(map(int, sys.stdin.readline().split())))

#최댓값 찾기
d = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, K+1):
    w = t[i][0]
    v = t[i][1]
    if j < w:
      d[i][j] = d[i-1][j]
    else:
      d[i][j] = max(d[i-1][j], v + d[i-1][j-w])

print(d[N][K])