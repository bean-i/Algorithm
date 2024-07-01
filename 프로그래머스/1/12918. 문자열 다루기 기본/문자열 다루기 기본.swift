func solution(_ s:String) -> Bool {
    if s.count == 4 || s.count == 6 {
        if let num = Int(s) {
            return true
        }
    }
    return false
}