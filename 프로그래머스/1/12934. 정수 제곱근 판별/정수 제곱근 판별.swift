import Foundation

func solution(_ n:Int64) -> Int64 {
    if let num = Int64(exactly: sqrt(Double(n))){
        return Int64(pow(Double(num+1), 2))
    }

    return -1
}