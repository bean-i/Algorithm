import sys
N = int(sys.stdin.readline())
word=[]
for _ in range(N):
  word.append(sys.stdin.readline().rstrip())
  
word = set(word)
word = list(word)

word.sort(key = lambda x:(len(x), x))
for i in word:
  print(i)