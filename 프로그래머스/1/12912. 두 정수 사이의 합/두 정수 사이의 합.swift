func solution(_ a:Int, _ b:Int) -> Int64 {
    var result: Int = 0
    var start: Int
    var end: Int
    
    if a < b {
        start = a
        end = b
    } else {
        start = b
        end = a
    }

    for num in start...end {
        result += num
    }
    return Int64(result)
}