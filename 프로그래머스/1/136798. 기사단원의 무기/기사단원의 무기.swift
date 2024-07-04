import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var answer = 0
    var a: [Int] = Array(repeating: 0, count: number+1)
    
    for i in 1...number {
        var d = i
        while d <= number {
            a[d] += 1
            d += i
        }
    }
    for now in a[1...] {
        if now > limit {
            answer += power
        } else {
            answer += now
        }
    }
    
    return answer
}