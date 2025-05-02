    let input = readLine()!.map { String($0) }
    var answer = 1 // 1씩 늘어가면서 N이 담길 변수
    var index = 0
    
    while true {
        let numbers = String(answer).map { String($0) }
        for number in numbers {
            if input[index] == number { index += 1 }
            if index >= input.count { break }
        }
        if index >= input.count { break }
        answer += 1
    }
    print(answer)