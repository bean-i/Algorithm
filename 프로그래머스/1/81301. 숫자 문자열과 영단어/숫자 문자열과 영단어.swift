import Foundation

func solution(_ s:String) -> Int {
    var result = ""
    let dic: [String:String] = ["zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"]
    var word = ""
    
    for char in s {
        if let num = Int(String(char)) {
            result += String(char)
        } else {
            word += String(char)
            if let w = dic[word] {
                result += w
                word = ""
            }
        }
    }

    return Int(result)!
}