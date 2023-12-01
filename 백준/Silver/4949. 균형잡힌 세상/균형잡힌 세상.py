import sys

while True:
  s = sys.stdin.readline()
  a = []
  if s=='.\n' and len(s)==2:
    break
  #입력받은 문자열에서 괄호만 따로 빼서 저장
  for i in range(len(s)):
    if s[i] == '(' or s[i] == '[':
      a.append(s[i])
    elif s[i] == ')':
      if len(a) != 0 and a[-1] == '(':
        a.pop()
      else:
        a.append(s[i])
        break
    elif s[i] == ']':
      if len(a) != 0 and a[-1] == '[':
        a.pop()
      else:
        a.append(s[i])
        break
  
  if len(a) == 0:
    print('yes')
  else:
    print('no')