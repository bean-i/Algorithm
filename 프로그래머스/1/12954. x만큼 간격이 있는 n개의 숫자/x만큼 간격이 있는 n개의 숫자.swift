func solution(_ x:Int, _ n:Int) -> [Int64] {
    var result: [Int64] = []
    var num = 0
    for i in 0..<n {
        result.append(Int64(num + x))
        num += x
    }
    return result
}