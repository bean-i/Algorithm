import math
def solution(progresses, speeds):
    answer = []
    days = []
    for i, j in zip(progresses, speeds):
        days.append(math.ceil((100-i)/j))
    
    num = days[0]
    cnt = 0
    for i in days:
        if i <= num:
            cnt+=1
        else:
            num = i
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    return answer