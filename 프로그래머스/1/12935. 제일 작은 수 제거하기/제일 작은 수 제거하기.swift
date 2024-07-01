func solution(_ arr:[Int]) -> [Int] {
    var result: [Int] = arr
    
    if let min = arr.min(), let index = arr.firstIndex(of: min) {
        result.remove(at: index)
    }
    if result.count > 0 { return result }
    else { return [-1] }
}