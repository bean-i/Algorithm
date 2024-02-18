
import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    
    idx = 0
    while True:
        first = heapq.heappop(q)
        if first >= K:
            return answer
        idx = first + heapq.heappop(q) * 2
        heapq.heappush(q, idx)
        answer += 1
        if len(q) == 1 and q[0] < K:
            return -1
    return answer