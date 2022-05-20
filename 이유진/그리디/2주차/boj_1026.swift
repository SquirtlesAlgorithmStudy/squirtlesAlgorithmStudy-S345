//
//  boj_1026.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/16.
//

import Foundation
//79516KB, 12ms
import Foundation

var N = Int(readLine()!)!

var maxCapacity = 0
var selectedRopeNum = 0
var inputA = [String]()
var inputB = [String]()

var arrayA = [Int]()
var arrayB = [Int]()

inputA = readLine()!.components(separatedBy: " ")
inputB = readLine()!.components(separatedBy: " ")

for i in 0...N-1{
    arrayA.append(Int(inputA[i])!)
    arrayB.append(Int(inputB[i])!)
  
   
}


arrayA.sort{return $0 > $1}
arrayB.sort{return $0 < $1}
var sum = 0
for i in 0...N-1{
    sum += arrayA[i]*arrayB[i]
}

print(sum)

