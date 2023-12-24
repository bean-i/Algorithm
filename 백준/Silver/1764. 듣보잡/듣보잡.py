import sys

N, M = map(int, sys.stdin.readline().split())
n = set()
m = set()

for _ in range(N):
  n.add(sys.stdin.readline().rstrip())

for _ in range(M):
  m.add(sys.stdin.readline().rstrip())

result = sorted(list(n&m))

print(len(result))
result.sort()
for i in result:
  print(i)