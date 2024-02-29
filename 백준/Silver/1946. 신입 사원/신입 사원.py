import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  score = []
  for _ in range(N):
    score.append(list(map(int, sys.stdin.readline().split())))

  score.sort()
  m = score[0][1]
  result = 1
  for i in range(1, len(score)):
    if score[i][1] < m:
      m = score[i][1]
      result += 1
  print(result)