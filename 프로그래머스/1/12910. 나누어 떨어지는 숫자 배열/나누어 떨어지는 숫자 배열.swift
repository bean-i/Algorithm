func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var result: [Int] = []
    for num in arr {
        if num % divisor == 0 {
            result.append(num)
        }
    }
    if result.count > 0 {
        return result.sorted()
    } else {
        return [-1]
    }
}