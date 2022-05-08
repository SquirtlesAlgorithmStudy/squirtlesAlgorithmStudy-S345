let n = Int(readLine()!)!
var cnt = 0
var money = 1000 - n

while true {
    if money == 0 {
        break
    }
    
    if money >= 500 {
        money -= 500
    } else if money >= 100 {
        money -= 100
    } else if money >= 50 {
        money -= 50
    } else if money >= 10 {
        money -= 10
    } else if money >= 5 {
        money -= 5
    } else if money >= 1 {
        money -= 1
    }
    
    cnt += 1
}

print(cnt)
