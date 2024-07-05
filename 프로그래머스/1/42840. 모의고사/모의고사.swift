import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let pattern1: [Int] = [1, 2, 3, 4, 5]
    let pattern2: [Int] = [2, 1, 2, 3, 2, 4, 2, 5]
    let pattern3: [Int] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    var answer: [Int:Int] = [1: 0, 2: 0, 3: 0]
    
    for (index, a) in answers.enumerated() {
        if pattern1[index%5] == a {answer[1]! += 1}
        if pattern2[index%8] == a {answer[2]! += 1}
        if pattern3[index%10] == a {answer[3]! += 1}
    }
    
    //max값 찾기
    var max = -1
    for a in answer {
        if a.value > max {
            max = a.value
        }
    }
    
    var result:[Int] = []
    for a in answer {
        if a.value == max {
            result.append(a.key)
        }
    }
    return result.sorted()
}