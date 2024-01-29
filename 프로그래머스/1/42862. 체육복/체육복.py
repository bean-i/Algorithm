def solution(n, lost, reserve):
    cnt = n - len(lost)
    lost.sort()
    reserve.sort()
    lost_copy = lost.copy()
    reserve_copy = reserve.copy()
    #여벌 옷 있으면서 도난 당한 학생 제거
    for i in reserve_copy:
        print('i: ', i)
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            cnt+=1
            
    print(lost)
    for i in reserve:
        for j in range(len(lost)):
            print(lost[j])
            if lost[j] == i-1 or lost[j] == i+1:
                del lost[j]
                cnt+=1
                break
            
    return cnt