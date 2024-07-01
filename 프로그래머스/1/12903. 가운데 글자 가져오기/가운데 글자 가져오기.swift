func solution(_ s:String) -> String {
    var a: Int
    var result: String = ""
    
    if s.count % 2 == 0 {
        a = s.count/2 - 1
        result += String(s[s.index(s.startIndex, offsetBy: a)])
        a += 1
        result += String(s[s.index(s.startIndex, offsetBy: a)])
    } else {
        a = s.count/2
        result += String(s[s.index(s.startIndex, offsetBy: a)])
    }
    return result
}