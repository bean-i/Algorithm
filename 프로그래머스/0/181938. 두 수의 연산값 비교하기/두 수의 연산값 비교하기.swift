import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let result1 = Int(String(a) + String(b))!
    let result2 = 2 * a * b
    
    if result1 > result2 {
        return result1
    } else {
        return result2
    }
}