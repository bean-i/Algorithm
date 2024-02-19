import sys

N = int(sys.stdin.readline())
rgb = []
for _ in range(N):
  rgb.append(list(map(int, sys.stdin.readline().split())))

#비용 저장 테이블
d = [[0] * 3 for _ in range(N)]
#첫 번째 집 비용 저장
for i in range(3):
  d[0][i] = rgb[0][i]
#순회 돌며, 최소 비용 업데이트
for i in range(1, N):
  #마지막 집의 색을 R로 칠할 경우
  d[i][0] = min(d[i-1][1], d[i-1][2]) + rgb[i][0]
  #마지막 집의 색을 G로 칠할 경우
  d[i][1] = min(d[i-1][0], d[i-1][2]) + rgb[i][1]
  #마지막 집의 색을 B로 칠할 경우
  d[i][2] = min(d[i-1][0], d[i-1][1]) + rgb[i][2]

print(min(d[N-1]))