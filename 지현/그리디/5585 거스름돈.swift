//
//  main.swift
//  1543 문서 검색
//
//  Created by 김지현 on 2022/05/09.
//

var change = 1000 - Int(readLine()!)!
var coin = [500, 100, 50, 10, 5, 1]
var num = 0

for i in coin {
    num += change / i
    change %= i
}
print(num)
