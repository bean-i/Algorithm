def solution(answers):
    answer = [0] * 3
    a1 = []
    a2 = []
    a3 = []
    l = len(answers)
    #학생별 찍은 답 저장
    for i in range(l):
        a1.append(i%5+1)
        
        if i%2 == 0:
            a2.append(2)
        elif i%8 == 1:
            a2.append(1)
        elif i%8 == 3:
            a2.append(3)
        elif i%8 == 5:
            a2.append(4)
        elif i%8 == 7:
            a2.append(5)
            
        if i%10 == 0 or i%10 ==1:
            a3.append(3)
        elif i%10 == 2 or i%10 ==3:
            a3.append(1)
        elif i%10 == 4 or i%10 == 5:
            a3.append(2)
        elif i%10 == 6 or i%10 ==7:
            a3.append(4)
        else:
            a3.append(5)
    #정답 맞힌 갯수 저장
    for i in range(l):
        if answers[i] == a1[i]:
            answer[0] += 1
        if answers[i] == a2[i]:
            answer[1] += 1
        if answers[i] == a3[i]:
            answer[2] += 1
    m = max(answer)
    result = []
    for i in range(3):
        if answer[i] == m:
            result.append(i+1)
    return result