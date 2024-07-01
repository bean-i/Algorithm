func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    var result: [[Int]] = []
    
    for (i, j) in zip(arr1, arr2) {
        var row: [Int] = []
        for (a, b) in zip(i, j) {
            row.append(a+b)
        }
        result.append(row)
    }
    return result
}