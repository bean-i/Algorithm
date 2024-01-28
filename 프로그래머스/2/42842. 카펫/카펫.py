def solution(brown, yellow):
    result = []
    cnt = brown + yellow
    for i in range(cnt, 0, -1):
        if cnt%i == 0:
            j = cnt//i
            if (i-2) * (j-2) == yellow:
                return [i, j]