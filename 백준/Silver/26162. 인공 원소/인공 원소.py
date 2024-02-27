import sys, math
import itertools
#소수 판별
def union(n):
  for i in range(2, n):
    if n%i == 0:
      return False
  return True

def check(a):
  r = []
  for i in range(2, a+1):
    if union(i):
      r.append(i)

  for i in range(len(r)):
    for j in range(i, len(r)):
      if r[i] + r[j] == a:
        return True
  return False
  

N = int(sys.stdin.readline())

for _ in range(N):
  a = int(sys.stdin.readline())
  if check(a):
    print('Yes')
  else:
    print('No')