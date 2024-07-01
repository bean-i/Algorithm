func solution(_ x:Int) -> Bool {
    var s = 0
    var num = x
    
    while num > 0 {
        s += num%10
        num /= 10
    }

    return x%s == 0
}