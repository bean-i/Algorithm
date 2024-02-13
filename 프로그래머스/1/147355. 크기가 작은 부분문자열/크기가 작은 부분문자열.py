def solution(t, p):
    cnt = 0
    l = len(p)
    array = []
    
    for i in range(len(t)-l+1):
        array.append(int(t[i:i+l]))
    for i in array:
        if i <= int(p):
            cnt+=1
    return cnt