import Foundation

let s1 = readLine()!

for a in s1 {
    if a.isLowercase{
        print(a.uppercased(), terminator: "")
    } else {
        print(a.lowercased(), terminator: "")
    }
}