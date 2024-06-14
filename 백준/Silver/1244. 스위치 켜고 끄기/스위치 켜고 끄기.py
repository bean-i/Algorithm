import sys

def switchNumber(i):
  if i == 0:
    return 1
  else:
    return 0

a = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline())
for _ in range(n):
  m, N = map(int, sys.stdin.readline().split())
  if m == 1:
    now = N
    while now <= a:
      switch[now-1] = switchNumber(switch[now-1])
      now += N
  elif m == 2:
    left, right = N-1, N+1
    switch[N-1] = switchNumber(switch[N-1])
    while left >= 1 and right <= a:
      if switch[left-1] == switch[right-1]:
        switch[left-1] = switchNumber(switch[left-1])
        switch[right-1] = switchNumber(switch[right-1])
        left -= 1
        right += 1
      else:
        break

for i in range(0, len(switch), 20):
  print(*switch[i:i+20])