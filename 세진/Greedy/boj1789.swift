//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/07.
//
// https://www.acmicpc.net/problem/1789

import Foundation

var input = Int(readLine()!)!
var cnt = 0

for x in 1...input {
    input -= x
    if input >= 0 {
        cnt += 1
    } else {
        break
    }
}
print(cnt)
