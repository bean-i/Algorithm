func solution(_ s:String) -> String {
    var result: String = ""
    
    if s.count % 2 == 0 {
        result += String(Array(s)[(s.count/2)-1...(s.count/2)])
    } else {
        result += String(Array(s)[s.count/2])
    }
    return result
}