import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
d = [0] * (N+1)

for i in range(1, N+1):
  for j in range(1, i+1):
    d[i] = max(d[i], d[i-j]+card[j-1])

print(d[N])