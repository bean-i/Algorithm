from collections import deque
def solution(maps):
    n = 0
    for i in maps:
        m = len(i)
        n+=1

    print(n, m)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return maps[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    return -1