import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var total = n
    var result = 0
    
    while total >= a {
        result += (total/a) * b
        total = (total/a)*b + total%a
    }
    
    return result
}