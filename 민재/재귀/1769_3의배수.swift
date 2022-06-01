//
//  1769_3의배수.swift
//  algo
//
//  Created by 김민재 on 2022/05/23.
//

// 재귀 x while문을 이용한 풀이방법
import Foundation

var input = readLine()!
var count = 0

while input.count > 1 {
    input = String(input.map { Int(String($0))! }.reduce(0){ $0 + $1 })
    count += 1
}

print(count)
if Int(input)! % 3 == 0 {
    print("YES")
} else {
    print("NO")
}
