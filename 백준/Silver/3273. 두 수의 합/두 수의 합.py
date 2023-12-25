import sys

N = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

result = 0
left, right = 0, N-1

while left < right:
  x1 = a[left] + a[right]
  if x1 == x:
    result += 1
    left += 1
  elif x1 < x:
    left += 1
  else:
    right -= 1

print(result)