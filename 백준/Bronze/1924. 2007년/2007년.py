import sys

x, y = map(int, sys.stdin.readline().split())

l = [1, 3, 5, 7, 8, 10, 12]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

cnt = -1
for i in range(1, x):
  if i == 2:
    cnt += 28
  elif i in l:
    cnt += 31
  else:
    cnt += 30
cnt+=y

print(day[cnt%7])