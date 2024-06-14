import sys

students = []

for _ in range(28):
  a = int(sys.stdin.readline())
  students.append(a)

students.sort()

for n in range(1, 31):
  if n not in students:
    print(n)