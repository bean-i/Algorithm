import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
tops = []
result = [0] * N

for i in range(N):
  while tops:
    if tops[-1][1] > num[i]:
      result[i] = tops[-1][0]+1
      break
    else:
      tops.pop()
  tops.append((i, num[i]))

print(*result)