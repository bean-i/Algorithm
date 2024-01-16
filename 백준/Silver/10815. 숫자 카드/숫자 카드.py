import sys

N = int(sys.stdin.readline())
sg = list(map(int, sys.stdin.readline().split()))
a = {}
for i in sg:
  a[i] = 0
  
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
b = {}
for i in check:
  b[i] = 0

for key in check:
  if key in a:
    print(1, end=' ')
  else:
    print(0, end=' ')