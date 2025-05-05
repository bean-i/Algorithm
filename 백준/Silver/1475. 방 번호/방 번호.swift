    let nums = readLine()!.map { Int(String($0))! }
    var numDict: [Int:Int] = [:]
    
    for i in 0..<10 {
        numDict[i] = 0
    }
    
    for num in nums {
        if num == 6 {
            numDict[9]! += 1
        }
        numDict[num]! += 1
    }
    
    if numDict[9]! > 0 {
        let num9 = numDict[9]! / 2
        let num6 = numDict[9]! - num9
        numDict[9]! = num9
        numDict[6]! = num6
    }
    
    print(numDict.sorted { $0.value > $1.value }.first!.value)