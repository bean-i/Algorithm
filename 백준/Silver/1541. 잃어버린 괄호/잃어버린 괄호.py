n1 = list(input().split('-'))
result = []
num = 0

if n1[0]=='':
  for i in range(1, len(n1)):
    n2 = list(map(int, n1[i].split('+')))
    result.append(sum(n2))
  for i in result:
    num -= i
    
else:
  for i in n1:
    n2 = list(map(int, i.split('+')))
    result.append(sum(n2))
  for i in range(len(result)):
    if(i==0):
      num+=result[i]
    else:
      num-=result[i]
    
  
print(num)