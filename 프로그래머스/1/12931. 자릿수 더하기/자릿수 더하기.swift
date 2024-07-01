import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    let str = String(n)
    for i in str {
        if let num = Int(String(i)) { answer += num}
    }
    
    return answer
}