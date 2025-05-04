    let N = Int(readLine()!)!
    var nums = readLine()!.split(separator: " ").map { Int($0)! }
    
    let repeatCount = Int(readLine()!)!
    
    for _ in 0..<repeatCount {
        let input = readLine()!.split(separator: " ").map { Int($0)! }
        if input[0] == 1 {
            male(nums: &nums, currentIndex: input[1])
        } else {
            female(nums: &nums, currentIndex: input[1])
        }
    }
    
    for i in stride(from: 0, to: nums.count, by: 20) {
        print(nums[i..<min(nums.count, i + 20)].map { String($0) }.joined(separator: " "))
    }
    
    func male(nums: inout [Int], currentIndex: Int) {
        var index = currentIndex
        let temp = index
        while index <= nums.count { // 조건 확인 필요
            nums[index - 1] = switchNum(num: nums[index - 1])
            index += temp
        }
    }
    
    func female(nums: inout [Int], currentIndex: Int) {
        var start = currentIndex
        var left = currentIndex - 1
        var right = currentIndex + 1
        
        nums[currentIndex - 1] = switchNum(num: nums[currentIndex - 1])
        
        
        while left - 1 >= 0 && right - 1 < nums.count {
            if nums[left - 1] == nums[right - 1] {
                nums[left - 1] = switchNum(num: nums[left - 1])
                nums[right - 1] = switchNum(num: nums[right - 1])
            } else {
                return
            }
            left -= 1
            right += 1
        }
    }
    
    func switchNum(num: Int) -> Int {
        if num == 0 { return 1 }
        return 0
    }