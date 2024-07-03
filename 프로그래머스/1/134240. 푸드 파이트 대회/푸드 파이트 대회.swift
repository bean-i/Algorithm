import Foundation

func solution(_ food:[Int]) -> String {
    var result: String = ""
    
    for (index, f) in food.enumerated() {
        if f < 2 {
            continue
        } else {
            for _ in 0..<f/2{
                result += String(index)
            }
        }
    }
    return result + "0" + String(result.reversed())
}