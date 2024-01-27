def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3

    for idx, value in enumerate(answers):
        if value == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if value == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if value == pattern3[idx%len(pattern3)]:
            score[2] += 1
            
    m = max(score)
    result = []
    for i in range(3):
        if score[i] == m:
            result.append(i+1)
    return result