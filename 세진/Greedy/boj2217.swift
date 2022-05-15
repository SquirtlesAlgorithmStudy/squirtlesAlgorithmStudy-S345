//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/15.
//
// https://www.acmicpc.net/problem/2217

import Foundation

let n = Int(readLine()!)!
var ropes = [Int]()

// n개 만큼의 로프 정보 가져오기
for _ in 0..<n {
    let rope = Int(readLine()!)!
    ropes.append(rope)
}

// 내림차순으로 정렬
ropes.sort(by: >)

var result = 0


for i in 0..<ropes.count {
    // i+1은 검사한 로프의 개수(현재 검사 중인 로프 포함)
    // 내림 차순으로 정렬했기 때문에 이전에 검사한 로프는 현재 검사 중인 로프보다 더 큰 중량을 가지는 로프이다.
    // 이전 로프까지 검사 했을 때 들어올릴 수 있는 최대 중량과 현재 검사중인 로프를 포함했을 때 가능한 최대 중량을 비교해서 result를 갱신한다.
    if (i+1) * ropes[i] > result {
        result = (i+1) * ropes[i]
    }
}

print(result)
