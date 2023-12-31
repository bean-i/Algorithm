import sys

N = int(sys.stdin.readline())
s=[0]*301
d=[0]*301
for i in range(N):
  s[i] = int(sys.stdin.readline())


d[0] = s[0]
d[1] = s[0]+s[1]
d[2] = max(s[0]+s[2], s[1]+s[2])

for i in range(3, N):
  d[i] = max(s[i-1]+s[i]+d[i-3], s[i]+d[i-2])

print(d[N-1])