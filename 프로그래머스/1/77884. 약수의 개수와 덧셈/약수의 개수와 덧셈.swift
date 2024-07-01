import Foundation

func count(_ num:Int) -> Int {
    var result = 0
    for i in 1...num {
        if num % i == 0 { result += 1 }
    }
    return result
}

func solution(_ left:Int, _ right:Int) -> Int {
    var result = 0
    
    for num in left...right {
        if count(num) % 2 == 0 {result += num}
        else {result -= num}
    }
    return result
}