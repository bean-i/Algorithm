let N = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let X = Int(readLine()!)!

let sortedArr = arr.sorted()

var left = 0
var right = N - 1

var currentSum = 0
var result = 0

while left < right {
    currentSum = sortedArr[left] + sortedArr[right]
    if currentSum == X {
        result += 1
        left += 1
    } else if currentSum < X {
        left += 1
    } else {
        right -= 1
    }
}

print(result)
