#4883
import sys

def find(dp):
  dp[1][0] += dp[0][1]
  dp[1][1] += min(dp[0][1], dp[0][1] + dp[0][2], dp[1][0])
  dp[1][2] += min(dp[0][1], dp[0][1] + dp[0][2], dp[1][1])
  for i in range(2, N):
    dp[i][0] += min(dp[i-1][0], dp[i-1][1])
    dp[i][1] += min(dp[i][0], dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][2] += min(dp[i][1], dp[i-1][1], dp[i-1][2])
  return dp[N-1][1]

i = 1
while True:
  N = int(sys.stdin.readline())
  if N == 0:
    break
  dp = []
  for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))
    
  a = find(dp)
  print("%d. %d" %(i, a))
  i += 1