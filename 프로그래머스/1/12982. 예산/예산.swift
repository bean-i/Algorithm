import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var fees = d
    var total = budget
    var result = 0
    fees.sort()
    
    for fee in fees {
        if total >= fee {
            total -= fee
            result += 1
        } else {
            return result
        }
    }
    return result
}