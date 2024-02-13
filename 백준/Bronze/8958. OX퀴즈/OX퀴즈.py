import sys
N = int(sys.stdin.readline())

for _ in range(N):
  s = sys.stdin.readline().rstrip()
  score = 0
  cnt = 1
  for i in s:
    if i == 'O':
      score += cnt
      cnt += 1
    elif i == 'X':
      cnt = 1
  print(score)