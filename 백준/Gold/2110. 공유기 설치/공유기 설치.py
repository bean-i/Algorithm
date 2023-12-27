import sys

N, C = map(int, sys.stdin.readline().split())
x = []

for _ in range(N):
  x.append(int(sys.stdin.readline().rstrip()))

x.sort()

start = 1
end = x[-1] - x[0]
result = 0

while (start<=end):
  mid = (start + end) // 2
  current = x[0]
  cnt = 1
  #공유기 심기
  for i in range(1, len(x)):
    if x[i] >= current + mid:
      cnt+=1
      current = x[i]
  if cnt >= C:
    start = mid+1
    result = mid
  else:
    end = mid-1

print(result)