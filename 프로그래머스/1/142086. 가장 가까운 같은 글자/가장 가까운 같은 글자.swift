import Foundation

func solution(_ s:String) -> [Int] {
    var result: [Int] = []
    var dic: [Character: Int] = [:]
    
    for (index, now) in s.enumerated() {
        if dic[now] == nil {
            dic[now] = index
            result.append(-1)
        } else {
            if let pre = dic[now] {
                result.append(index - pre)
            }
            dic[now] = index
        }
    }
    return result
}