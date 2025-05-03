    let input = readLine()!.split(separator: " ").map { Int($0)! }
    var coins: [Int] = []
    
    // input[0] = n
    // input[1] = k
    
    for _ in 0..<input[0] { // 동전, 오름차순 정렬
        let coin = Int(readLine()!)!
        coins.append(coin)
    }
    
    // k보다 작은 동전 화폐중에 가장 큰 값을 찾아서 최대한 많이 쓰기
    // k 4200 -> 1000*4 -> 200
    coins.reverse()
    var answer = 0
    var remain = input[1]
    for coin in coins {
        answer += remain / coin
        remain = remain % coin
    }
    print(answer)