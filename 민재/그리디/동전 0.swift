//
//  동전 0.swift
//  algo
//
//  Created by 김민재 on 2022/05/07.
//

import Foundation

let nums = readLine()!.split(separator: " ").map {Int($0)!}
let n = nums[0]
var k = nums[1]

var coins: [Int] = []


for _ in 0 ..< n {
    let price = Int(readLine()!)!
    coins.append(price)
}

coins = coins.reversed()

var cnt = 0
for coin in coins {
    
    if coin <= k {
        cnt += k / coin
        k %= coin
    }
    
}

print(cnt)
