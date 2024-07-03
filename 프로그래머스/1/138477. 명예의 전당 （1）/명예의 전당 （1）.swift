import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var save: [Int] = []
    var result: [Int] = []
    
    for sc in score {
        if save.count < k {
            save.append(sc)
        } else {
            save.sort()
            if sc > save[0] {
                save.remove(at: 0)
                save.append(sc)
            }
        }
        result.append(save.min()!)
    }
    return result
}