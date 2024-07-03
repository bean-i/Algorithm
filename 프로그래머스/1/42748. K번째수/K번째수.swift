import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var start: Int
    var end: Int
    var wh: Int
    var result: [Int] = []
    
    for com in commands {
        start = com[0]
        end = com[1]
        wh = com[2]
        result.append(array[start-1..<end].sorted()[wh-1])
    }
    return result
}