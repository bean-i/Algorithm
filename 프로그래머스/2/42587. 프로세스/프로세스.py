from collections import deque

def solution(priorities, location):
    queue = deque()
    answer = []
    #큐에 중요도, 순서 저장
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    #큐 돌면서 정렬
    while queue:
        m = max(queue)[0]
        if queue[0][0] == m:
            answer.append(queue[0])
            queue.popleft()
        else:
            now = queue.popleft()
            queue.append(now)
    #최종 순서 찾기
    for i in range(len(answer)):
        if answer[i][1] == location:
            return i+1