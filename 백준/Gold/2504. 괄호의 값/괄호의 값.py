import sys

s = list(sys.stdin.readline().rstrip())

stack = []
cnt = 1
result = 0
for i in range(len(s)):
  if s[i] == '(':
    cnt *= 2
    stack.append(s[i])
  elif s[i] == '[':
    cnt *= 3
    stack.append(s[i])
  elif s[i] == ')':
    if not stack or stack[-1] =='[':
      result = 0
      break
    if s[i-1] == '(':
      result += cnt
    stack.pop()
    cnt //= 2
  elif s[i] == ']':
    if not stack or stack[-1] =='(':
      result = 0
      break
    if s[i-1] == '[':
        result += cnt
    stack.pop()
    cnt //= 3

if stack:
  result = 0

print(result)