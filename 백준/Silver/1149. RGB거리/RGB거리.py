import sys

N = int(sys.stdin.readline())
home = []
for _ in range(N):
  home.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
  home[i][0] = min(home[i][0] + home[i-1][1], home[i][0] + home[i-1][2])
  home[i][1] = min(home[i][1] + home[i-1][0], home[i][1] + home[i-1][2])
  home[i][2] = min(home[i][2] + home[i-1][0], home[i][2] + home[i-1][1])
  
print(min(home[N-1]))