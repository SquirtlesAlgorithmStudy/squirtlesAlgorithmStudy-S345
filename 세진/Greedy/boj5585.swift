//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/06.
//

// https://www.acmicpc.net/problem/5585
import Foundation

var input = Int(readLine()!)!

var change = 1000 - input

let money = [500, 100, 50, 10, 5, 1]

var cnt = 0

for x in money {
    cnt += change / x
    change %= x
}

print(cnt)
