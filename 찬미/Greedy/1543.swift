var word = readLine()!
var searchWord = readLine()!

var index = 0
var cnt = 0

while word.count - index >= searchWord.count {
    let startIndex = word.index(word.startIndex, offsetBy: index)
    let endIndex = word.index(startIndex, offsetBy: searchWord.count-1)
    if word[startIndex...endIndex] == searchWord {
        cnt += 1
        index += searchWord.count
    } else {
        index += 1
    }
}

print(cnt)
