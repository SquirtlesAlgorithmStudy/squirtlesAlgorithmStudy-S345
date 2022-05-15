//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/15.
//
// https://www.acmicpc.net/problem/1026

import Foundation

let n = Int(readLine()!)!
var a = readLine()!.split(separator: " ").map({ Int($0)! })
var b = readLine()!.split(separator: " ").map({ Int($0)! })

a.sort() // 오름차순 정렬
b.sort(by: >) // 내림차순 정렬

var result = 0

for i in 0..<n {
    result += a[i]*b[i]
}

print(result)
