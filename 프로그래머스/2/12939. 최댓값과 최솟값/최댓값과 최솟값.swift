func solution(_ s:String) -> String {
    let nums = s.split(separator: " ").map{Int($0)!}
    if let a = nums.min(), let b = nums.max() {
        return "\(a) \(b)"
    }
    return ""
}