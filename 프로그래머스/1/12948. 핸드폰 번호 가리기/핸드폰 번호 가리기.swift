func solution(_ phone_number:String) -> String {
    let cnt = phone_number.count - 4
    let result = Array(repeating: "*", count: cnt).joined() + phone_number.suffix(4)
    
    return result
}