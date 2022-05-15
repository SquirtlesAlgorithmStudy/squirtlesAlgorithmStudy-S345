//
//  1931.swift
//  algorithm
//
//  Created by 황찬미 on 2022/05/15.
//

import Foundation

let number = Int(readLine()!)!
var times: [(Int, Int)] = []

for _ in 1...number {
    let input = readLine()!.split(separator: " ").map {Int($0)!}
    
    times.append((input[0], input[1]))
}

// 시작하는 시간을 기준으로 정렬을 한 후, 끝나는 시간을 기준으로 정렬을 하는 로직 사용...
times.sort(by: { $0.0 < $1.0 }) // 시작하는 시간 기준 오름차순
times.sort(by: { $0.1 < $1.1 }) // 끝나는 시간 기준 오름차순

var endTime = 0
var cnt = 0

for time in times {
    if time.0 >= endTime {
        endTime = time.1
        cnt += 1
    }
}

print(cnt)
