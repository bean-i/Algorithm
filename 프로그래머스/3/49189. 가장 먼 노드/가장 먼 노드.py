from collections import deque
INF = int(1e9)
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [[INF, i] for i in range(n+1)]
    
    for i in edge:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(n+1):
        graph[i].sort()
    
     
    #bfs
    distance[1][0] = 0
    q = deque([1])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i][0] == INF:
                distance[i][0] = distance[now][0] + 1
                q.append(i)

    distance = [dist[0] for dist in distance[1:]]
    return distance.count(max(distance))