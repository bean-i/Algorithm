def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        a = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]:
                a += 1
            else:
                break
        answer.append(a)
        
                
    return answer