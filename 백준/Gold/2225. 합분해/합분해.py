import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

#dp[0][N]은 0개로 N을 만드는 법의 개수이므로 모든 값 0
#dp[K][0]은 N개의 수로 0을 만드는 법의 개수이므로 모든 값 1로 초기화
for i in range(1, K+1):
  dp[i][0] = 1

#dp 테이블 업데이트
for i in range(1, K+1):
  for j in range(1, N+1):
    dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[K][N]%1000000000)