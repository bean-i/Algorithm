import sys

N = int(sys.stdin.readline())

dp = [0] * 10001

dp[1] = 1
dp[2] = 3
dp[3] = 5
cnt = 2

for i in range(3, N+1):
  dp[i] = (dp[i-1] + dp[i-2]*2) % 10007

print(dp[N]%10007)