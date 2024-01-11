import sys

N = int(sys.stdin.readline())
h = []

for _ in range(N):
  x, y = map(int, sys.stdin.readline().split())
  h.append((x, y))

h.sort()

for i in range(1, len(h)):
  a, b = h[i-1]
  x, y = h[i]
  if a <= x <= b and a <= y <= b:
    h[i] = (a, b)
    h[i-1] = (0, 0)
  elif a <= x <= b:
    if y >= b:
      h[i] = (a, y)
      h[i-1] = (0, 0)
  elif a <= y <= b:
    if x <= a:
      h[i] = (x, b)
      h[i-1] = (0, 0)
  elif x <=a or x >= b:
    continue

result = 0
for i in range(len(h)):
  a, b = h[i]
  result += b-a
  
print(result)
