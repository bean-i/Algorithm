extension String {
    subscript (_ num: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: num)]
    }
}

func solution(_ strings:[String], _ n:Int) -> [String] {
    
    var result: [String:Int] = [:]
    
    for (index, s) in strings.enumerated() {
        result[s] = index
    }
    
    return result.sorted {
        if $0.key[n] == $1.key[n] {
            return $0 < $1
        } else {
            return $0.key[n] < $1.key[n]
        }
    }.map{$0.key}
}