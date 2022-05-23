//
//  main.swift
//  Implementation
//
//  Created by User on 2022/05/23.
//

import Foundation

var wheels = [[0,0,0,0,0,0,0,0]]
for _ in 0...3 {
    let wheel = Array(readLine()!).map({ Int(String($0))! })
    wheels.append(wheel)
}

let n = Int(readLine()!)!

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map({ Int(String($0))! })
    let wheelNum = input[0]
    let direction = input[1]
    
    // 한 톱니바퀴를 회전시키면 연쇄적으로 다른 톱니바퀴를 회전시켜야 하는데...
}



print(wheels)
