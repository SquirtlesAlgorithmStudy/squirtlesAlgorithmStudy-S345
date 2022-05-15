//
//  main.swift
//  algo
//
//  Created by 김민재 on 2022/05/03.
//

import Foundation

let n = Int(readLine()!)!

var money = 1000 - n
var cnt = 0

while money > 0 {
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
    } else {
        money -= 1
    }
    cnt += 1
}

print(cnt)
