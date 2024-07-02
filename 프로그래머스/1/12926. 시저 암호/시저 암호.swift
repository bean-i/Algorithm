func solution(_ s:String, _ n:Int) -> String {
    var result = ""
    
    for ch in s {
        if ch == " " {
            result += " "
            continue
        }
        
        if let ascii = UnicodeScalar(String(ch))?.value {
            var shifted: UInt32 = 0
            
            if (65...90).contains(ascii) { // 대문자
                shifted = (ascii - 65 + UInt32(n)) % 26 + 65
            } else if (97...122).contains(ascii) { // 소문자
                shifted = (ascii - 97 + UInt32(n)) % 26 + 97
            }
            
            if let newChar = UnicodeScalar(shifted) {
                result.append(Character(newChar))
            }
        }
    }
    return result
}