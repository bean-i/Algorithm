def solution(s):
    a = []
    for i in range(len(s)):
        a.append(s[i])
        if len(a) >= 2:
            if a[-1] == ')' and a[-2] == '(':
                a.pop()
                a.pop()
            
    if len(a) == 0:
        answer = True
    else:
        answer = False
        
    return answer

# solution('(())())')