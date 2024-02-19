import sys

N = int(sys.stdin.readline())
d = []

#삼각형 값 받기
tri = []
for _ in range(N):
  tri.append(list(map(int, sys.stdin.readline().split())))

d.append([tri[0][0]])
for i in range(1, N):
  d.append([0 for _ in range(i+1)])
  for j in range(len(tri[i])):
    if j == 0:
      d[i][j] = d[i-1][j] + tri[i][j]
    elif j == i:
      d[i][j] = d[i-1][j-1] +  tri[i][j]
    else:
      d[i][j] = max(d[i-1][j-1], d[i-1][j]) + tri[i][j]
    
print(max(d[N-1]))