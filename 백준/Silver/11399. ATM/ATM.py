n = int(input())

p = list(map(int, input().split()))
p.sort()

result = 0
for i in p:
  result += i*n
  n-=1

print(result)