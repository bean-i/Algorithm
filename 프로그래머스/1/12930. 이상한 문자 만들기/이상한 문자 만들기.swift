extension String {
    subscript (_ n: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: n)]
    }
    subscript (_ range: Range<Int>) -> String {
        let fromIndex = self.index(self.startIndex, offsetBy: range.startIndex)
        let toIndex = self.index(self.startIndex,offsetBy: range.endIndex)
        return String(self[fromIndex..<toIndex])
    }
}

func solution(_ s:String) -> String {
    var result = ""
    var index = 0
    for c in s {
        if c == " "{
            index = 0
            result.append(c)
            continue
        } else if index % 2 == 0 {
            result.append(c.uppercased())
            index += 1
        } else {
            result.append(c.lowercased())
            index += 1
        }
    }
    return result
}