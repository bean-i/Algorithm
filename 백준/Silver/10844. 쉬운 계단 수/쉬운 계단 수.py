import sys

N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
  #끝 자리가 0인 경우 => 끝에서 앞자리는 1만 올 수 있음
  dp[i][0] = dp[i-1][1] % 1000000000
  #끝 자리가 9인 경우 => 끝에서 앞자리는 8만 올 수 있음
  dp[i][9] = dp[i-1][8] % 1000000000
  #끝 자리가 1~8인 경우
  for j in range(1, 9):
    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
    
print(sum(dp[N])% 1000000000)