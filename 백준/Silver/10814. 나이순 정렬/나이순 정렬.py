import sys
N = int(sys.stdin.readline())
mem=[]
for _ in range(N):
  mem.append(list(sys.stdin.readline().split()))

mem.sort(key=lambda x:int(x[0]))

for i in mem:
  print(i[0], i[1])