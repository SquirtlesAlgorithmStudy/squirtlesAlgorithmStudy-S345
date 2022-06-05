//
//  보물.swift
//  algo
//
//  Created by 김민재 on 2022/05/13.
//

import Foundation


let n = Int(readLine()!)!

var A = readLine()!.split(separator: " ").map {Int($0)!}
var B = readLine()!.split(separator: " ").map {Int($0)!}


A.sort(by: >)
B.sort(by: <)

var answer = 0
for i in 0..<n{
    answer += A[i] * B[i]
}

print(answer)

