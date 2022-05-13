//
//  main.swift
//  1543 문서 검색
//
//  Created by 김지현 on 2022/05/09.
//

var num = Int(readLine()!)!
var count = 0

while true {
    if num % 5 == 0 {
        print(num/5 + count)
        break
    } else {
        num -= 3
        count += 1
        if num == 0 {
            print(count)
            break
        } else if num < 0 {
            print(-1)
            break
        }
    }
}
