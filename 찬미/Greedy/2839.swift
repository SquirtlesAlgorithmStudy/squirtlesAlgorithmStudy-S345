var n = Int(readLine()!)!
var cnt = 0

while true {
    if n % 5 == 0 {
        cnt += (n / 5)
        break
    }
    n -= 3
    cnt += 1
    
    if n < 0 {
        cnt = -1
        break
    }
}

print(cnt)
