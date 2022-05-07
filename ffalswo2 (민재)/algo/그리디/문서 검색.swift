//
//  File.swift
//  algo
//
//  Created by 김민재 on 2022/05/07.
//

// 문자열에서 target 마지막 문자열 index 찾고 마지막 문자열 Index + 1 부터 다시 찾음
import Foundation

var string = readLine()!
var targetString = readLine()!

var endIndex = string.range(of: targetString)?.upperBound

var count = 0

while endIndex != nil {
    count += 1
    string = String(string[endIndex!...])
    endIndex = string.range(of: targetString)?.upperBound
}

print(count)
