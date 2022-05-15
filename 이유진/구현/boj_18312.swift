//
//  boj_18312.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/15.
//

import Foundation

var N = Int()
var K = Int()
if let input = readLine() {
    let arrInput = input.components(separatedBy: " ")
    N = Int(arrInput[0])!
    K = Int(arrInput[1])!
}
var count = 0
for h in 0...N{
    for m in 0...59{
        for s in 0...59{
            if (h/10 == K || h%10 == K ||
                m/10 == K || m%10 == K ||
                s/10 == K || s%10 == K){
                count+=1
            }else{
                continue
            }
        }
    }
}

print(count)
