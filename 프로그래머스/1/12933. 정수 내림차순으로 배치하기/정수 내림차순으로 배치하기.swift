func solution(_ n:Int64) -> Int64 {
    var result = Array(String(n)).sorted(by: >).compactMap{ String($0) }.joined()
    if let answer = Int64(result) { return answer }
    return 0
}