import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in A:
  dic[i] = 1

for i in check:
  if i in dic:
    print(1)
  else:
    print(0)