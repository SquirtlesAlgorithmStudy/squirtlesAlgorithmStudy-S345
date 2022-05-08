//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/07.
//

// https://www.acmicpc.net/problem/11047

var input = readLine()!.split(separator: " ").map({ Int($0)! })

var n = input[0]
var k = input[1]
var coins = [Int]()
var cnt = 0

for _ in 0..<n {
    let coin = Int(readLine()!)!
    coins.append(coin)
}

coins.sort(by: >)

for coin in coins {
    if coin > k {
        continue
    }
    
    cnt += k / coin
    k %= coin
    
    if k == 0 {
        break
    }
}

print(cnt)
