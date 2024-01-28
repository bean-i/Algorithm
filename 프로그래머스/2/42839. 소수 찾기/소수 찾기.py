def back(M, numbers, array="", used=set(), result=set()):
    if len(array) == M:
        num = int(array)
        if check(num):
            result.add(num)
        return
    for i in range(len(numbers)):
        if i in used:
            continue
        used.add(i)
        back(M, numbers, array + numbers[i], used, result)
        used.remove(i)

#소수 판별        
def check(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        

def solution(numbers):
    result = set()
    ans = []
    nums = []
    
    
    for i in range(1, len(numbers) + 1):
        back(i, numbers, "", set(), result)
    
    return len(result)
    
                