import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd = ""
    var even = ""
    for num in num_list {
        if num % 2 == 0 {
            even += String(num)
        }else {
            odd += String(num)
        }
    }
    
    return Int(even)! + Int(odd)!
}