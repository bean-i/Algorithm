import Foundation
var input = readLine()!
let d = input.split(separator: " ").compactMap { Double($0) }

let sum = d.reduce(0, +)
print(String(format: "%.6f", sum))