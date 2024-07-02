import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var x = 0
    var y = 0
    
    for size in sizes {
        let a = size[0] < size[1] ? size[1] : size[0]
        let b = size[0] > size[1] ? size[1] : size[0]
        if a > x {x = a}
        if b > y {y = b}
    }
    return x*y
}