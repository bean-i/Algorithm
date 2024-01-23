def solution(clothes):
    dict = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dict:
            dict[clothes[i][1]] += 1
        else:
            dict[clothes[i][1]] = 1
    
    cnt = 1
    for value in dict.values():
        cnt *= (value+1)


    return cnt-1

# for i in range(len(clothes)):
#         print(clothes[i])
#         if clothes[i][1] in dict:
#             dict[clothes[i][1]].append(clothes[i][0])
#         else:
#             dict[clothes[i][1]] = clothes[i][0]