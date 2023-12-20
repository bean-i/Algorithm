import sys
N = int(sys.stdin.readline())
s=[]
#길이, 자릿수의 합, 알파벳 순
for _ in range(N):
  a = sys.stdin.readline().rstrip()
  sum = 0
  for i in a:
    if i.isdigit():
      sum+=int(i)
  s.append((a, sum))

s.sort(key=lambda x:(len(x[0]), x[1], x[0]))

for i in s:
  print(i[0])