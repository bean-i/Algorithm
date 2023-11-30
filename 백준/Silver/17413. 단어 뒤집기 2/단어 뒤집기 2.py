s = input()

s = s.replace('<', '@<')
s = s.replace('>', '>@')

words = s.split('@')

for i in words:
  if i=='':
    continue
  if i[0]!='<':
    result = []
    space = i.split(' ')
    for j in space:
      result.append(j[::-1])
    print(" ".join(result), end='')
  else:
    print(i, end='')