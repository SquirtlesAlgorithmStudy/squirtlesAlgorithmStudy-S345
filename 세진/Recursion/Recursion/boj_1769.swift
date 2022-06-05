//
//  main.swift
//  Recursion
//
//  Created by User on 2022/05/23.
//
// https://www.acmicpc.net/submit/1769

import Foundation

var input = readLine()!

func isMultipleOfThree(num: String) {
    if num.count == 1 {
        print(cnt)
        if Int(num)! % 3 == 0 { print("YES") }
        else { print("NO") }
    } else {
        cnt += 1
        isMultipleOfThree(num: sumOfEachDigit(num))
    }
}

// 각 자리의 수를 더한 값을 반환하는 함수 (String으로 반환)
func sumOfEachDigit(_ n: String) -> String {
    return String(n.map({ String($0) }).reduce(0, {$0 + Int($1)!}))
}

var cnt = 0
isMultipleOfThree(num: input)
