import Foundation

let s = Int(readLine()!)!

var total = 0
var cnt = 0

for i in 1...s {
    total += i
    cnt += 1
    if total > s {
        print(cnt - 1)
        break
    } else if total == s {
        print(cnt)
        break
    }
}

