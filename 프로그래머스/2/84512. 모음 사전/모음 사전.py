from itertools import product

def solution(word):
    dic = []
    for i in range(1, 6):
        for j in product('AEIOU', repeat=i):
            dic.append(''.join(j))
    dic.sort()
    for i, j in enumerate(dic):
        if j == word:
            return i+1