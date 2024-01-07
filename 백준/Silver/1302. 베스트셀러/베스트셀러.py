import sys

N = int(sys.stdin.readline())
s = {}
for _ in range(N):
  word = sys.stdin.readline().rstrip()
  if word in s:
    s[word] += 1
  else:
    s[word] = 1

s = sorted(s.items(), key = lambda x:(-x[1], x[0]))
print(s[0][0])