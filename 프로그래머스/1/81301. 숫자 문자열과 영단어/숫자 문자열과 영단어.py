eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
def findEng(find):
    for j in range(len(eng)): #index
        if find == eng[j]:
            return str(j)
    return False
        

def solution(s):
    answer = ''
    find = ''
    for i in s:
        if i in num:
            answer += i
        else:
            find += i
        if find in eng:
                answer += findEng(find)
                find=''
    
    return int(answer)