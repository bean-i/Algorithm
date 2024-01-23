def solution(citations):
    
    citations.sort(reverse = True)
    
    if max(citations) == 0:
        return 0
    
    for h in range(len(citations), -1, -1):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                cnt += 1
                if cnt == h:
                    return cnt
            else:
                break

    
    
# citations.sort(reverse = True)
#     m = citations[0]
#     for h in range(len(citations), -1, -1):
#         i = 0
#         cnt = 0
#         for j in range(len(citations)):
#             if citations[j] < h:
#                 i = j
#                 break
#         up = citations[:i]
#         if min(up) >= h and len(up) >= h:
#             return h