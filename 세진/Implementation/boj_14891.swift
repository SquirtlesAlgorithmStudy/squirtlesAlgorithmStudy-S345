//
//  main.swift
//  Implementation
//
//  Created by User on 2022/05/23.
//
// https://www.acmicpc.net/problem/14891

import Foundation

var wheels = [[Int]]()

for _ in 0...3 {
    let wheel = Array(readLine()!).map({ Int(String($0))! })
    wheels.append(wheel)
}

// 맞닿는 왼쪽 부분
let leftPointIndex = 6
// 맞닿는 오른쪽 부분
let rightPointIndex = 2
// 전체 톱니바퀴 개수
let wheelCnt = 4

let n = Int(readLine()!)!

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map({ Int(String($0))! })
    let wheelNum = input[0] - 1
    let direction = input[1]

    var ch = Array(repeating: false, count: wheelCnt)
    rotate(wheelNum: wheelNum, isClockwise: direction, ch: &ch)
}

var result = 0

for (index, wheel) in wheels.enumerated() {
    if index == 0 {
        if wheel[0] == 1 { result += 1 }
    } else if index == 1 {
        if wheel[0] == 1 { result += 2 }
    } else if index == 2 {
        if wheel[0] == 1 { result += 4 }
    } else if index == 3 {
        if wheel[0] == 1 { result += 8 }
    }
}

print(result)



func rotate(wheelNum: Int, isClockwise: Int, ch: inout [Bool]) {
    ch[wheelNum] = true
    
    let nextWheelNum = wheelNum + 1
    let beforeWheelNum = wheelNum - 1
    
    // 오른쪽 톱니 바퀴 회전
    if nextWheelNum < wheelCnt && !ch[nextWheelNum] && wheels[wheelNum][rightPointIndex] != wheels[nextWheelNum][leftPointIndex] {
        rotate(wheelNum: nextWheelNum, isClockwise: -isClockwise, ch: &ch)
    }
    
    // 왼쪽 톱니 바퀴 회전
    if beforeWheelNum >= 0 && !ch[beforeWheelNum] && wheels[wheelNum][leftPointIndex] != wheels[beforeWheelNum][rightPointIndex] {
        rotate(wheelNum: beforeWheelNum, isClockwise: -isClockwise, ch: &ch)
    }
    
    rotateWheel(wheelNum: wheelNum, isClockwise: isClockwise)
}

func rotateWheel(wheelNum: Int, isClockwise: Int) {
    // 시계 방향
    if isClockwise == 1 {
        let temp = wheels[wheelNum].removeLast()
        wheels[wheelNum].insert(temp, at: 0)
    } else { // 반시계 방향
        let temp = wheels[wheelNum].removeFirst()
        wheels[wheelNum].append(temp)
    }
}

