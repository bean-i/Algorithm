import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
NGE = [-1]*N
idx = [0]

for i in range(1, N):
  while idx and a[idx[-1]] < a[i]:
    NGE[idx.pop()] = a[i]
  idx.append(i)

print(*NGE)