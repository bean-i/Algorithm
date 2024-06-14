import sys

N = int(sys.stdin.readline())

dic = {}

for _ in range(N):
  file = list(map(str, sys.stdin.readline().strip().split('.')))
  if file[1] in dic:
    dic[file[1]] += 1
  else:
    dic[file[1]] = 1

dic = sorted(dic.items())
for i in dic:
  print(i[0], i[1])