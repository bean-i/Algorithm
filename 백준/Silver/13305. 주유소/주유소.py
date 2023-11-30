N = int(input())

d = list(map(int, input().split()))
price = list(map(int, input().split()))
min = price[0]
result = 0

for i in range(len(price)-1):
  if price[i] < min:
    min = price[i]
  result += min*d[i]

print(result)