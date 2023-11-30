n1 = list(input().split('-'))
result = []

for i in n1:
  n2 = list(map(int, i.split('+')))
  result.append(sum(n2))

num = result[0]
for i in range(1, len(result)):
  num -= result[i]

print(num)