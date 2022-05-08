//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/06.
//

// https://www.acmicpc.net/problem/2839

import Foundation
var weight = Int(readLine()!)!
var cnt = 0

while true {
    if weight % 5 == 0 {
        cnt += weight / 5
        break
    }
    weight -= 3
    cnt += 1
    
    if weight < 0 {
        cnt = -1
        break
    }
}
print(cnt)
