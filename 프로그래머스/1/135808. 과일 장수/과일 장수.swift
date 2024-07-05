import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    var scores = score.sorted(by: >)
    var nowSum = 0
    
    for index in stride(from: 0, to: scores.count, by: m) {
        if index + m <= scores.count {
            nowSum += scores[index..<index+m].min()!*m
        }
    }  
    return nowSum
}