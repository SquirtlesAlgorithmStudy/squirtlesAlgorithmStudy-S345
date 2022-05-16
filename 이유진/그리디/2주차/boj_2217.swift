//
//  boj_2217.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/16.
//

import Foundation

var N = Int()

if let input = readLine(){
    N = Int(input)!
}
var arrRopeCapcity = [Int]()
var maxCapacity = 0
var selectedRopeNum = 0
for i in 0...N-1{
    arrRopeCapcity.append( Int(readLine()!)!)
}

arrRopeCapcity.sort{return $0>$1}

maxCapacity = arrRopeCapcity[0]
selectedRopeNum = 1

var newMaxCapacity = 0
for i in 1...arrRopeCapcity.count - 1{
    selectedRopeNum += 1
    newMaxCapacity = arrRopeCapcity[i]*selectedRopeNum

    if (newMaxCapacity > maxCapacity){
        maxCapacity = newMaxCapacity
        continue
    }else{
        break
    }
}

print(maxCapacity)
