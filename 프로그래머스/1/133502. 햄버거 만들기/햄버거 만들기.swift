import Foundation

func solution(_ ingredient:[Int]) -> Int {
    
    var stack: [Int] = []
    var answer = 0
    
    for i in ingredient	{
        stack.append(i)
        if Array(stack.suffix(4)) == [1, 2, 3, 1] {
            stack.removeLast(4)
            answer += 1
        }
    }
    
    return answer
}