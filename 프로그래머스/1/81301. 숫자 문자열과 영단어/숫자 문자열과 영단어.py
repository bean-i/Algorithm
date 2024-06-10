def solution(s):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(eng)):
        s = s.replace(eng[i], str(i))
        
    return int(s)