import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    var result = ""
    result = my_string.prefix(s) + overwrite_string
    let index = s + overwrite_string.count
    result += my_string.suffix(my_string.count - index)

    return result
}