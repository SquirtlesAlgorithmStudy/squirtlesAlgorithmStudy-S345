//
//  main.swift
//  1543 문서 검색
//
//  Created by 김지현 on 2022/05/09.
//

var s = Int(readLine()!)!
var n = 1

while n*(n+1) / 2 <= s { n += 1 }
print( n-1 )
