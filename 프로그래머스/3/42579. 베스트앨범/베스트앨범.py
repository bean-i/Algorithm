import heapq
def solution(genres, plays):
    answer = []
    dict = {}
    sumplay = {}
    
    for i, j, k in zip(genres, plays, range(len(plays))):
        if i in dict:
            heapq.heappush(dict[i], [-j, k])
            sumplay[i] += j
        else:
            #재생횟수, 고유번호
            dict[i] = []
            heapq.heappush(dict[i], [-j, k])
            sumplay[i] = j
    
    sorted_sumplay = [k[0] for k in sorted(sumplay.items(), key = lambda x:x[1], reverse=True)]
    
    for key in sorted_sumplay:
        for _ in range(2):
            if dict[key]:
                a, b = heapq.heappop(dict[key])
                answer.append(b)
            else:
                break
            
    return answer