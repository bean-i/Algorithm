import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d=[1]*N

for i in range(N):
  for j in range(0, i):
    if a[j] < a[i]:
      d[i] = max(d[i], d[j]+1)

print(max(d))

max_d = max(d)
result=[]
for i in range(N-1, -1, -1):
  if d[i] == max_d:
    result.append(a[i])
    max_d -= 1

result.reverse()
for i in result:
  print(i, end=' ')