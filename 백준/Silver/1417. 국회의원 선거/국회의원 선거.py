import sys
N = int(sys.stdin.readline())
a = []
for _ in range(N):
  a.append(int(sys.stdin.readline()))

ds = a[0]
cnt=0
if len(a) <= 1:
  print(cnt)

else:
  back = a[1:]
  while True:
    if ds > max(back):
      break
    else:
      cnt+=1
      idx = back.index(max(back))
      ds += 1
      back[idx] -= 1
  print(cnt)