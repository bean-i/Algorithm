import sys

x, y = map(int, sys.stdin.readline().split())

l = [1, 3, 5, 7, 8, 10, 12]
s = [4, 6, 9, 11]

cnt = y
for i in range(x):
  if i in l:
    cnt += 31
  elif i in s:
    cnt += 30
  else:
    cnt += 28

result = cnt % 7

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day[result])