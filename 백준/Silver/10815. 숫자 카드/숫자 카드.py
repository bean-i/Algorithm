import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
q = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in A:
  dic[i] = 1

answer = []
for i in q:
  if i in dic:
    answer.append(1)
  else:
    answer.append(0)

print(*answer)