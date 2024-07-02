import Foundation

extension String {
    subscript (_ range: Range<Int>) -> String {
        let fromIndex = self.index(self.startIndex, offsetBy: range.startIndex)
        let toIndex = self.index(self.startIndex, offsetBy: range.endIndex)
        return String(self[fromIndex..<toIndex])
    }
}

func solution(_ t:String, _ p:String) -> Int {
    var result = 0
    
    let cntP = p.count
    let cntT = t.count
    
    let long = cntP < cntT ? cntT : cntP
    let short = cntP > cntT ? cntT : cntP

    for i in 0...long-short {
        if let num = Int(t[i..<i+cntP]), let numP = Int(p) {
            if num <= numP {
                result += 1
            }
        }
    }
    return result
}