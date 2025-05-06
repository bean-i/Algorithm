    let N = Int(readLine()!)!
    var answer = Array(repeating: Array(repeating: ".", count: N), count: N)
    var result = Array(repeating: Array(repeating: ".", count: N), count: N)
    
    for i in 0..<N {
        let str = readLine()!.map { String($0) }
        for index in 0..<N {
            answer[i][index] = str[index]
        }
    }
    
    for i in 0..<N {
        let str = readLine()!.map { String($0) }
        for index in 0..<N {
            result[i][index] = str[index]
        }
    }
    
    for (index, (a, b)) in zip(answer, result).enumerated() {
        for i in 0..<N {
            if b[i] == "." { continue }
            else if a[i] == ".", b[i] == "x" {
                // 상하좌우대각선 확인
                checkBombNum(x: index, y: i, answer: &answer, result: &result)
            } else if a[i] == "*", b[i] == "x" {
                checkBomb(answer: &answer, result: &result)
            }
        }
    }

    for i in 0..<N {
        print(result[i].joined())
    }
    
    func checkBombNum(x: Int, y: Int, answer: inout [[String]], result: inout [[String]]) {
        var count = 0
        var list: [String] = []
        let dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        let dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        for i in 0..<8 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if nx >= 0 && nx < N && ny >= 0 && ny < N {
                list.append(answer[nx][ny])
            }
        }

        count = list.filter { $0 == "*" }.count
        result[x][y] = String(count)
    }

    func checkBomb(answer: inout [[String]], result: inout [[String]]) {
        for i in 0..<N {
            for j in 0..<N {
                if answer[i][j] == "*" {
                    result[i][j] = "*"
                }
            }
        }
    }