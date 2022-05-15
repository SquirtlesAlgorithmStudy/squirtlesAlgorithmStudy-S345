//
//  main.swift
//  Implementation
//
//  Created by User on 2022/05/15.
//

// https://www.acmicpc.net/problem/18312

import Foundation

let input = readLine()!.split(separator: " ").map({ Int($0)! })
let n = input[0]
let k = input[1]
var cnt = 0

// xx시xx분xx초 형태로 변환 후 k를 포함하는지 확인
func check(hour: Int, minute: Int, second: Int, value: Int) -> Bool {
    var hourString = String(hour)
    var minuteString = String(minute)
    var secondString = String(second)
    
    if hourString.count == 1 { hourString.insert("0", at: hourString.startIndex) }
    if minuteString.count == 1 { minuteString.insert("0", at: minuteString.startIndex) }
    if secondString.count == 1 { secondString.insert("0", at: secondString.startIndex) }
    
    if "\(hourString)\(minuteString)\(secondString)".contains(String(k)) {
        return true
    }
    
    return false
}


for hour in 0...n {
    for minute in 0..<60 {
        for second in 0..<60 {
            // String.contains(value)는 해당 String이 value를 포함하고 있으면 true를 return
            if check(hour: hour, minute: minute, second: second, value: k) {
                cnt += 1
            }
        }
    }
}



print(cnt)
