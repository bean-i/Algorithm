import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var plus = 0
    var result: Set<Int> = []
    
    for i in 0..<numbers.count {
        for j in i+1..<numbers.count {
            plus = numbers[i] + numbers[j]
            result.update(with: plus)
        }
    }

    return result.sorted()
}