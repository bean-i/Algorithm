import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var fee = 0
    for i in 1...count {
        fee += price*i
    }
    if fee >  money {
        return Int64(fee - money)
    } else {
        return 0
    }
}