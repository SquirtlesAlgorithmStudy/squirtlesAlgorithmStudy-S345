//
//  boj_11047.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/08.
//

import Foundation

var N = Int()
var K = Int()
var coinSystem = [Int]()
var count = 0

if let input = readLine() {
    var array = input.components(separatedBy: " ")
    N = Int(array[0])!
    K = Int(array[1])!
}
for i in 0...N-3{
    if let input = readLine(){
        coinSystem.append(Int(input)!)
      //  coinSystem[i] = Int(input)!
    }
}

for i in (0...coinSystem.count-1).reversed(){
    print(i)
    count += K/coinSystem[i]
    K = K%coinSystem[i]
}
print(count)

