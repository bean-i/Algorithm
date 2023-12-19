n, m = map(int, input().split())
a = list(map(int, input().split()))

max=0
for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      c = a[i] + a[j] + a[k]
      if c<=m and c>max:
        max = c
print(max)