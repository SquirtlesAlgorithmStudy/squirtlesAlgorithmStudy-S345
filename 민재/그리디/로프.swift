//
//  로프.swift
//  algo
//
//  Created by 김민재 on 2022/05/12.
//

import Foundation


let n = Int(readLine()!)!

var weights: [Int] = []

for _ in 0..<n {
    weights.append(Int(readLine()!)!)
}


weights = weights.sorted { $0 >= $1 }


var low = 10001
var total = 0

for i in 0..<weights.count {
    // 작은 중량 찾기
    low = min(low, weights[i])

    // 이전에 계산된 값, 로프 갯수 * 작은 중량, 해당 로프가 들수있는 중량 중 가장 큰 값
    total = max(total, (i+1) * low, weights[i])
}

print(total)





func otherSolution() {
    let n = Int(readLine()!)!

    var weights: [Int] = []

    for _ in 0..<n {
        weights.append(Int(readLine()!)!)
    }


    weights = weights.sorted { $0 >= $1 }

    var total = 0

    for i in 0..<weights.count {
        total = max(total, weights[i] * (i+1))
    }

    print(total)
}


