func solution(_ a:Int, _ b:Int) -> String {
    var cal: [Int:Int] = [1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31]
    let day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    var sum = 0
    
    if a > 1 {
        for i in 1...a-1 {
            sum += cal[i]!
        }
    }
    
    let dist = (sum + b - 1)%7
    
    return day[dist]
}