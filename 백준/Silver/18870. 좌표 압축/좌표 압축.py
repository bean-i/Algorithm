import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

dx = sorted(list(set(X)))
dic = {dx[i]: i for i in range(len(dx))}

for i in X:
  print(dic[i], end=' ')