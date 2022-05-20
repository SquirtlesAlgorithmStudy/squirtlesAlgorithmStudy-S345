//
//  시각.swift
//  algo
//
//  Created by 김민재 on 2022/05/15.
//

import Foundation

let input = readLine()!.split(separator: " ").map {Int($0)!}
let N = input[0]
let K = input[1]


func makeString(number: Int) -> String {
    var twoString: String = "\(number)"
    if number < 10 {
        twoString = "0\(number)"
    }
    
    return twoString
}


var answer = 0
for h in 0...N {
    let hour = makeString(number: h)
    for m in 0..<60 {
        let minute = makeString(number: m)
        for s in 0..<60 {
            let second = makeString(number: s)
            if (hour + minute + second).contains("\(K)") {
                answer += 1
            }
        }
    }
}

print(answer)


