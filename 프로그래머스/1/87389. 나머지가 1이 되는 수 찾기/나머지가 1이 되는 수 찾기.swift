import Foundation

func solution(_ n:Int) -> Int {
    var result: [Int] = []
    for i in 2...n {
        if n%i == 1{
            result.append(i)
        }
    }
    result.sort()
    return result[0]
}