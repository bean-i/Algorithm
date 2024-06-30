import Foundation

func solution(_ s:String) -> Bool
{
    var cntP = 0
    var cntY = 0
    for i in s{
        if i == "P" || i == "p" {
            cntP += 1
        } else if i == "Y" || i == "y" {
            cntY += 1
        }
    }
    
    if cntP == cntY { return true }
    else { return false }

}