def back(l, ans, dungeons, k, result):
    if len(ans) == l:
        cnt = 0
        for j in ans:
            if k >= dungeons[j][0]:
                cnt+=1
                k -= dungeons[j][1]
        result.append(cnt)
        return
    for i in range(l):
        if i not in ans:
            ans.append(i)
            back(l, ans, dungeons, k, result)
            ans.pop()

def solution(k, dungeons):

    l = len(dungeons)
    ans = []
    result = []
    back(l, ans, dungeons, k, result)

    return max(result)