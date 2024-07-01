import Foundation

func solution(_ n:Int64) -> Int64 {
    let result = Int64(sqrt(Double(n)))
    return result * result == n ? (result + 1) * (result + 1) : -1
}