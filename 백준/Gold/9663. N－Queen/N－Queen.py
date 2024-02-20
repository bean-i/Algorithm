import sys

def is_safe(row, col):
  for i in range(row):
    if board[i] == col or abs(board[i] - col) == abs(i - row):
      return False
  return True

def add(row):
  global count
  #모든 행에 퀸을 배치했으면 끝
  if row == N:
    count += 1
    return
  #모든 열에 대해 백트랙킹
  for col in range(N):
    if is_safe(row, col):
      board[row] = col
      add(row+1)

N = int(sys.stdin.readline())
board = [-1] * N
count = 0
add(0)
print(count)