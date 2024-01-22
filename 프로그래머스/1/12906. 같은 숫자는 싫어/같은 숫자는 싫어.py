def solution(arr):
    answer = [arr[0]]
    num = arr[0]
    for i in arr:
        if i == num:
            continue
        else:
            answer.append(i)
            num = i
    
    return answer