n, k = map(int, input().split())
cnt = 0
coin = []

for _ in range(n):
  coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
  if k//i >= 1:
    cnt += k//i
    k -= i*(k//i)

print(cnt)