//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/07.
//

// https://www.acmicpc.net/problem/1543

import Foundation

var document = readLine()!
var word = readLine()!

var cnt = 0
var index = 0

while document.count - index >= word.count {
    let start = document.index(document.startIndex, offsetBy: index)
    let end = document.index(start, offsetBy: word.count-1)
    if document[start...end] == word {
        cnt += 1
        index += word.count
    } else {
        index += 1
    }
}

print(cnt)
