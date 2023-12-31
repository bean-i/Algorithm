import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [1] * N

for i in range(len(a)):
  for j in range(0, i):
    if a[j] < a[i]:
      d[i] = max(d[i], d[j]+1)

print(max(d))