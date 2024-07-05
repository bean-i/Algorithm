import Foundation

func solution(_ n:Int) -> Int {
    var array = Array(repeating: true, count: n + 1)
    array[0] = false
    array[1] = false
    let end = Int(sqrt(Double(n)))
    
    for i in 2...end+1 {
        if array[i] == true {
            var j = 2
            while i*j <= n {
                array[i*j] = false
                j += 1
            }
        }
    }
    return array.filter{$0 == true}.count
}