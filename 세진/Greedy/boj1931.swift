//
//  main.swift
//  Greedy
//
//  Created by User on 2022/05/15.
//
// https://www.acmicpc.net/problem/1931

import Foundation

let n = Int(readLine()!)!
var meetings = [[Int]]()

for _ in 0..<n {
    let meeting = readLine()!.split(separator: " ").map({ Int($0)! })
    meetings.append(meeting)
}

meetings.sort {
    if $0[1] == $1[1] {
        return $0[0] < $1[0]
    }
    return $0[1] < $1[1]
}

var previousEndTime = 0
var cnt = 0

for meeting in meetings {
    if meeting[0] >= previousEndTime {
        cnt += 1
        previousEndTime = meeting[1]
    }
}

print(cnt)

