import Foundation

extension String {
    subscript(i: Int) -> Character {
        return self[index(startIndex, offsetBy: i)]
    }
}

func solution(_ my_string:String, _ index_list:[Int]) -> String {
    var result = ""
    for index in index_list {
        result += String(my_string[index])
    }
    return result
}