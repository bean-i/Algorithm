import Foundation

func solution(_ dartResult:String) -> Int {
    //최종 숫자 저장
    var result: [Int] = []
    //result에 저장하기 전 저장공간
    var n: String = ""
    var end = 0
    
    for i in dartResult {
        if let num = Int(String(i)) {
            n += String(i)
        } else if i == "S" {
            result.append(Int(n)!)
            n = ""
        } else if i == "D" {
            result.append(Int(pow(Double(n)!, 2)))
            n = ""
        } else if i == "T" {
            result.append(Int(pow(Double(n)!, 3)))
            n = ""
        } else if i == "*" {
            end = result.count-1
            //2 이상이면
            for j in 0..<2 {
                if end >= 0 {
                    result[end] *= 2
                    end -= 1
                }
            }
        } else if i == "#" {
            end = result.count-1
            result[end] = 0 - result[end]
        }
    }
    
    return result.reduce(0, +)
}