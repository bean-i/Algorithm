import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
  a[i] = max(a[i], a[i]+a[i-1])

print(max(a))