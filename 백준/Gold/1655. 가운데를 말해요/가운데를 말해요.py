import sys, heapq

N = int(sys.stdin.readline())
left_h = []
right_h = []

for i in range(1, N+1):
  a = int(sys.stdin.readline())
  if len(left_h) == len(right_h):
    heapq.heappush(left_h, -a)
  else:
    heapq.heappush(right_h, a)
  if right_h and -left_h[0] > right_h[0]:
    x = -heapq.heappop(left_h)
    y = heapq.heappop(right_h)
    heapq.heappush(left_h, -y)
    heapq.heappush(right_h, x)
  print(-left_h[0])
  # print('a: ', a)
  # print('mid: ', -left_h[0])
  # print('left: ', left_h)
  # print('right: ', right_h)