import sys
N = int(sys.stdin.readline())
cnt=0

while N>0:
  if N%5 == 0:
    cnt += N//5
    N -= N//5 * 5
  else:
    N -= 3
    if N < 0:
      cnt=-1
      break
    cnt+=1
print(cnt)