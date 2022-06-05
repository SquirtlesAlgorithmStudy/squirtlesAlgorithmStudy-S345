while true {
    let input = readLine()!
    var flag = true
    // . 찍을 경우 문장 끝내기
    if input == "." {
        break
    }
    var stack: [String.Element] = []
    
    for i in input {
        // 괄호가 열렸을 경우 stack에 추가
        if i == "[" || i == "(" {
            stack.append(i)
        } else if i == "]" || i == ")" {
            // 이 밑에부터는 어떻게 코드를 짜면 좋을지 잘 모르겠네요 . . .
            // [ 와 ]만 짝이 될 수 있고, (와 )만 짝이 될 수 있는데
            // [이 나오고 )인 경우는 어떻게 구분을 해 줄 수 있을지?
            // 그 반대로 (이 나오고 ]이 나온 경우는…?
        }
    }
}
