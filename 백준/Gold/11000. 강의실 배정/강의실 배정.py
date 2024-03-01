import sys, heapq

N = int(sys.stdin.readline())

cl = []
answer = []

for _ in range(N):
  cl.append(list(map(int, sys.stdin.readline().split())))

cl.sort()
answer = []

heapq.heappush(answer, cl[0][1])

for i in range(1, N):
  #새로 들어오는 수업 시작값이 더 작으면 새 강의실 개설
  if cl[i][0] < answer[0]:
    heapq.heappush(answer, cl[i][1])
  #뒤이어 할 수 있다면, 강의 끝나는 시간 업데이트
  else:
    heapq.heappop(answer)
    heapq.heappush(answer, cl[i][1])

print(len(answer))

# 5
# 1 3
# 2 4
# 3 5
# 4 9
# 5 7