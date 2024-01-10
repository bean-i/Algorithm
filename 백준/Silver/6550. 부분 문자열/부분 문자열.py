import sys

while True:
  try:
    s, t = list(sys.stdin.readline().split())

    cnt=0
    w=0
    for i in range(len(s)):
      flag = 0
      for j in range(w, len(t)):
        if s[i] == t[j]:
          cnt+=1
          w=j+1
          flag=1
          break
      if flag == 0:
        break
    
    if cnt == len(s):
      print('Yes')
    else:
      print('No')
  except:
    break