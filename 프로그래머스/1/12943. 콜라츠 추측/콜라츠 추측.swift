func odd(_ num:Int) -> Int {
    return num*3 + 1
}

func even(_ num:Int) -> Int {
    return num/2
}

func solution(_ num:Int) -> Int {
    var result = 0
    var n = num
    while n != 1 {
        if result >= 500 { return -1 }
        if n%2 == 0 {
            n = even(n)
            result += 1
        } else {
            n = odd(n)
            result += 1
        }
    }
    return result
}