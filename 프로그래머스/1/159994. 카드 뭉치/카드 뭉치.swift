import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    
    var now1 = 0
    var now2 = 0
    var nowG = 0
    
    while now1 < cards1.count || now2 < cards2.count {
        if now1 < cards1.count && cards1[now1] == goal[nowG] {
            now1 += 1
            nowG += 1
        } else if now2 < cards2.count && cards2[now2] == goal[nowG] {
            now2 += 1
            nowG += 1
        } else {
            return "No"
        }
        if nowG == goal.count {
            return "Yes"
        }
    }
    
    return ""
}