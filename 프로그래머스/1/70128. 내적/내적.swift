import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result = 0
    for (x, y) in zip(a, b) {
        result += x*y
    }
    return result
}