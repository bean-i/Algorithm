    let N = Int(readLine()!)!
    
    for _ in 0..<N {
        
        let input = readLine()!.split(separator: " ").map { Int($0)! }
        let caseNum = input[0]
        var students = Array(input[1..<input.count])
        
        var results: [Int] = []
        let cnt = sortCount(results: &results, students: &students)
        print(caseNum, cnt)
    }
    
    func sortCount(results: inout [Int], students: inout [Int]) -> Int {
        
        var count = 0
        
        for (index, student) in students.enumerated() {
            results.append(student)
            for (indexR, result) in results.enumerated() {
                if result > student {
                    results.insert(student, at: indexR)
                    results.removeLast()
                    count += index - indexR
                    break
                }
            }
        }
        return count
    }