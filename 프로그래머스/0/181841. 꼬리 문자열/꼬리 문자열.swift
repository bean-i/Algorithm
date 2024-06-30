import Foundation

func solution(_ str_list:[String], _ ex:String) -> String {
    var result = ""
    for s in str_list {
        if s.contains(ex){
            continue
        } else {
            result += s
        }
    }
    return result
}