import sys

N, score, P = map(int, sys.stdin.readline().split())
if N > 0 :
  s = list(map(int, sys.stdin.readline().split()))
else:
  print(1)
  exit()

s.append(score)
s.sort(reverse=True)

result = s.index(score) + 1

if N == P and s[-1] >= score:
  print(-1)
elif result <= P:
  print(result)