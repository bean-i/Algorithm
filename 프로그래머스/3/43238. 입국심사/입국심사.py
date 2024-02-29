def solution(n, times):
    answer = 0
    left  = min(times)
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        result = 0
        for i in times:
            result += mid//i
        if result >= n:
            answer = mid
            right = mid - 1
        elif result < n:
            left = mid + 1
    return answer