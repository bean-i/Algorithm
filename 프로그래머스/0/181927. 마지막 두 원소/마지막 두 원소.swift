import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var result = num_list
    let a = num_list[num_list.count-2]
    let b = num_list[num_list.count-1]
    
    if b > a {
        result.append(b-a)
    } else {
        result.append(b*2)
    }
    return result
}