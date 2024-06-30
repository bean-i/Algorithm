func solution(_ s:String) -> Int {
    let str = s.components(separatedBy:"-")
    
    if let result = str.last, let num = Int(result) {
        if str.count > 1{ return 0-num }
        else { return num }
    }
    return 0
}