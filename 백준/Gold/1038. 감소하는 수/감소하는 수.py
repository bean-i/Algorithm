import sys
from itertools import combinations

N = int(sys.stdin.readline())

nums = []
for i in range(1, 11):
  for c in combinations(range(0, 10), i):
    c = list(c)
    c.sort(reverse = True)
    nums.append(int("".join(map(str, c))))

nums.sort()
if N < len(nums):
  print(nums[N])
else:
  print(-1)