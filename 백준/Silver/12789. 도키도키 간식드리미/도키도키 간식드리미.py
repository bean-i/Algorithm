import sys
N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
w = []
cnt = 1
for i in range(len(s)):
  if s[i] == cnt:
    cnt+=1
    if w:
      for _ in range(len(w)):
        if w[-1] == cnt:
          cnt+=1
          w.pop()
    continue
  else:
    w.append(s[i])

if w:
  print('Sad')
else:
  print('Nice')