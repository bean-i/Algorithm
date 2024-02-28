from collections import deque
#두 단어의 알파벳 일치 개수 구하기
def count(word, new):
    cnt = 0
    for i in range(len(word)):
        if word[i] == new[i]:
            cnt += 1
    return cnt
    
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [0] * len(words)
    while q:
        word, cnt = q.popleft()

        if word == target:
            return cnt
        for i in range(len(words)):
            if not visited[i]:
                #만약 i가 word와 한글자 차이라면, 큐에 저장
                if count(word, words[i]) == len(word) - 1:
                    q.append((words[i], cnt+1))
                    visited[i] = 1
    return 0