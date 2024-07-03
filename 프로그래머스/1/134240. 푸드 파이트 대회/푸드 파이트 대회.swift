import Foundation

func solution(_ food:[Int]) -> String {
    var result: String = ""
    
    for (index, f) in food.enumerated() {
        if f >= 2 {
            result += String(repeating: String(index), count:f/2)
        }
    }
    return result + "0" + String(result.reversed())
}