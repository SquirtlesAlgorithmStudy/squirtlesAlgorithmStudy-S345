let num = readLine()!.split(separator: " ").map { Int($0)! }
let n = num[0]
var k = num[1]

var coins: [Int] = []
var cnt = 0

for _ in 0..<n {
    coins.append(Int(readLine()!)!)
}

coins = coins.reversed()

for coin in coins {
    if coin <= k {
        cnt += (k / coin)
        k %= coin
    }
}

print(cnt)
