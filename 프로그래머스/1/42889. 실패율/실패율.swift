import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var result: [Int:Int] = [:]
    var answer: [Int:Double] = [:]
    var total = stages.count
    
    stages.forEach{ result[$0, default: 0] += 1 }
    
    for i in 1...N {
        if let now = result[i] {
            answer[i] = Double(now) / Double(total)
            total -= now
        } else {
            answer[i] = 0
        }
    }
    
    return answer.sorted { 
        if $0.value == $1.value {
            return $0.key < $1.key
        } else {
            return $0.value > $1.value
        }
    }.map { $0.key }
}