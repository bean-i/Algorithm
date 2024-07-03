import Foundation

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer = Array(String(repeating: " ", count: n))
    var result: [String] = []
    var result1: [Character] = []
    var result2: [Character] = []
    
    for (num1, num2) in zip(arr1, arr2) {
        answer = Array(String(repeating: " ", count: n))
        result1 = Array(String(num1, radix: 2))
        result2 = Array(String(num2, radix: 2))
        
        if result1.count < n {
            while result1.count != n {
                result1.insert("0", at: 0)
            }
        }
        if result2.count < n {
            while result2.count != n {
                result2.insert("0", at: 0)
            }
        }

        for index in 0..<result1.count {
            if result1[index] == "1" {
                answer[index] = "#"
            }
        }
        for index in 0..<result2.count {
            if result2[index] == "1" && answer[index] == " "{
                answer[index] = "#"
            }
        }
        result.append(String(answer))
    }
    return result
}