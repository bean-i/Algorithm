import Foundation

extension String {
    subscript(index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

func solution(_ str1:String, _ str2:String) -> String {
    var result = ""
    for index in 0..<str1.count {
        result += String(str1[index]) + String(str2[index])
    }
    return result
}