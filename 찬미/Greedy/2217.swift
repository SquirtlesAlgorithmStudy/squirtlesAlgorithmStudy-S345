//
//  2217.swift
//  algorithm
//
//  Created by 황찬미 on 2022/05/15.
//

import Foundation

let number = Int(readLine()!)!
var ropes: [Int] = []
var result = 0

for _ in 1...number {
    ropes.append(Int(readLine()!)!)
}

// 문제에서 최대라는 단어가 나왔을 경우, 배열을 내림차순으로 정렬해 둔 후 구현하는 것이 좋다는 조언을 듣고 내림차순으로 구현.
ropes.sort(by: > )

// 문제가 이해가 안 가요 . . . 😂
for _ in 0...<number {

}
