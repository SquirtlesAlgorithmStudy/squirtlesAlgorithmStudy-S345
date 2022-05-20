//
//  18312.swift
//  algorithm
//
//  Created by 황찬미 on 2022/05/15.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int($0)!})
let N = input[0]
let K = input[1]

var mandscnt = 0
var hcnt = 0
var result = 0

// 분과 초에서 K를 발견할 경우 cnt 추가
for m in 0..<60 {
    for s in 0..<60 {
        if (m % 10 == K || m / 10 == K || s % 10 == K || s / 10 == K) {
            mandscnt += 1
        }
    }
}

// h에서 K를 발견할 경우 cnt 추가
for h in 0..<23 {
    if h % 10 == K || h / 10 == K {
        hcnt += 1
    }
}

result = mandscnt + (hcnt * 3600)
print(result)

// 5 3 입력시, 8775 출력...
// 무엇을 놓쳤을까요 . . .
