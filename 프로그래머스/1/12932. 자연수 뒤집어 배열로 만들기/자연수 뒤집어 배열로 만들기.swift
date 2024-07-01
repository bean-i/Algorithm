func solution(_ n:Int64) -> [Int] {
    let strArray = Array(String(n))
    var result: [Int] = []
    for i in strArray.reversed() {
        result.append(Int(String(i))!)
    }

    return result
}