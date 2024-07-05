import Foundation

func find(_ n:Int) -> Bool {
    for i in 2..<n {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func solution(_ nums:[Int]) -> Int {
    var answer = 0
    
    for i in 0..<nums.count {
        for j in i+1..<nums.count {
            for k in j+1..<nums.count {
                if find(nums[i]+nums[j]+nums[k]) {
                    answer += 1
                }
            }
        }
    }

    return answer
}