//
//  main.swift
//  Algorithm_Week2
//
//  Created by 김지현 on 2022/05/15.
//

import Foundation

/*
 정수 N과 K가 입력되었을 때 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 K가 하나라도 포함되는 모든 시각을 세는 프로그램을 작성하시오. 시각을 셀 때는 디지털 시계를 기준으로, 초 단위로만 시각을 구분한다.

 예를 들어 K=3일 때, 다음의 시각들은 3이 하나 이상 포함되어 있으므로 세어야 하는 시각의 대표적인 예시이다.

 23시 00분 00초
 07시 08분 33초
 반면에 다음의 시각들은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 예시이다.

 15시 02분 55초
 18시 27분 45초
 */

var input = readLine()!.split(separator: " ").map { Int($0)! }
var N = input[0]
var K = input[1]

var count = 0
var kInN = 0
var mAndS = 0

for m in 0..<60 {
    for s in 0..<60 {
        if (m / 10 == K || m % 10 == K ||
            s / 10 == K || s % 10 == K) {
            mAndS += 1
        }
    }
}

for n in 0...N {
    (n / 10 == K || n % 10 == K) ? kInN += 1 : nil
}

count = (N - kInN + 1) * mAndS + kInN * 3600

print(count)

// 1. 59분 59초 까지 k가 포함되는 개수 = default -> 3600
// 2, N에 K가 포함되는 개수 = kInN -> 24
// 3, (n-kInN+1) * default + kInN * 60*60

//var count = 0
//var minute = 60
//var second = 60
//
//for n in 0...N {
//    for m in 0..<minute {
//        for s in 0..<second {
//            if (n / 10 == K || n % 10 == K ||
//                m / 10 == K || m % 10 == K ||
//                s / 10 == K || s % 10 == K) {
//                count += 1
//
//            }
//        }
//    }
//}
//
//print(count)
