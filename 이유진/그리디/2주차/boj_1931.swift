//
//  boj_1931.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/16.
//

import Foundation

var N = Int(readLine()!)!

var time = [[Int]](repeating: Array(repeating: 0,count: 2 ), count: N)
var input = [String]()

var startTime = Int()
var endTime = Int()

for i in 0...N-1{
    input = readLine()!.components(separatedBy: " ")
    startTime = Int(input[0])!
    endTime = Int(input[1])!
    time.append([startTime,endTime])
}
time.sort{$0[0] < $1[0]}

var maxNum = 0

for i in 0...N-2{
    if(time[i+1][0]>=time[i][1]){
        maxNum += 1
    }
}


