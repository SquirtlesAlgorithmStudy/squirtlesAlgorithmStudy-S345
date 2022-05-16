//
//  1026.swift
//  보물
//  algorithm
//
//  Created by 황찬미 on 2022/05/15.
//

import Foundation

let input = Int(readLine()!)!

let A = readLine()!.split(separator: " ").map({Int($0)!})
let B = readLine()!.split(separator: " ").map({Int($0)!})

// A를 내림차순, B를 오름차순으로 정렬해 주어도 최솟값이 나오기 때문에 두 배열을 모두 정렬해 주었습니다.
// B의 재배열을 하지 않고 푸는 방법은 무엇이 있을까요?
var A_sort = A.sorted(by: >) // 0 1 1 1 6
var B_sort = B.sorted(by: <) // 8 7 3 2 1

var sum = 0
    
// removeLast()함수는 마지막 값을 return 하고 그 값을 지우는 함수.
// 값이 무조건 있는 경우에만 사용하여야 한다.
// *** 추가로 popLast() 함수도 있는데, 이 함수는 값이 없을 경우 nil을 반환한다.
// 옵셔널 값을 반환하기 때문에 옵셔널 바인딩을 통해 옵셔널 값을 안전하게 꺼내주는 과정이 필요하다.

for _ in 1...input {
    sum += A_sort.removeLast() * B_sort.removeLast()
}

print(sum)
