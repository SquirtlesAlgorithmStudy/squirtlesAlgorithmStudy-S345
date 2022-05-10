//
//  11047 동전 0.swift
//  1543 문서 검색
//
//  Created by 김지현 on 2022/05/09.
//

let temp = readLine()!.split(separator: " ").map{Int($0)!}
let n = temp[0]
var k = temp[1]

var coins = [Int]()
for _ in 0..<n {
    coins.append(Int(readLine()!)!)
}

coins = coins.reversed()

var answer = 0

for i in coins {
    if i <= k {
        answer += (k / i)
        k = k % i
    }
    
    if k == 0 {
        break
    }
}

print(answer)
