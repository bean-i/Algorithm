import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
  c =  sys.stdin.readline().split()
  
  if c[0] == '1':
    stack.append(c[1])
    
  elif c[0] == '2':
    if stack:
      print(stack.pop())
    else:
      print('-1')
  elif c[0] == '3':
    print(len(stack))
  elif c[0] == '4':
    if stack:
      print('0')
    else:
      print('1')
  elif c[0] == '5':
    if stack:
      print(stack[-1])
    else:
      print('-1')
      