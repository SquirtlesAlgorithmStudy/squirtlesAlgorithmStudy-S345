//
//  회의실 배정.swift
//  algo
//
//  Created by 김민재 on 2022/05/13.
//

import Foundation

let n = Int(readLine()!)!


var meetings = [[Int]]()
for _ in 0..<n {
    let data = readLine()!.split(separator: " ").map {Int($0)!}
    meetings.append(data)
}


meetings.sort {
    if $0[1] == $1[1] {
        return $0[0] < $1[0]
    }
    return $0[1] <= $1[1]
}


var answer = 0 // 3
var lateTime = 0 // 5 -> 6 -> 7
var lastEndTime = 0 // 5 -> 6

for meeting in meetings {
    let startTime = meeting[0] // 7,7
    let endTime = meeting[1]
    
    lateTime = max(lateTime, endTime)
    
    if startTime >= lastEndTime && lateTime == endTime {
        answer += 1
        lastEndTime = endTime
    }
}

print(answer)


