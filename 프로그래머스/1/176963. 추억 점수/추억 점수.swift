import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var names: [String:Int] = [:]
    var result: [Int] = []
    var s = 0
    
    for (n, score) in zip(name, yearning) {
        names[n] = score
    }
    
    for i in photo {
        s = 0
        for j in i {
            if let now = names[j] {
                s += now
            }
        }
        result.append(s)
    }

    return result
}