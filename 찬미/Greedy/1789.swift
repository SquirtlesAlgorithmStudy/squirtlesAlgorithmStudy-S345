let n = Int(readLine()!)!
var sum = 0
var cnt = 0

for i in 1...n {
    sum += i
    cnt += 1
    
    if sum > n {
        cnt -= 1
        break
    } else if sum == n {
        break
    }
}

print(cnt)
