//
//  설탕배달.swift
//  algo
//
//  Created by 김민재 on 2022/05/03.
//

import Foundation


func solution() -> Int {
    var input = Int(readLine()!)!
    var cnt = 0
    if input % 5 == 0 {
        return input / 5
    }
    
    while input > 0 {
        input -= 3
        cnt += 1
        if input % 5 == 0 {
            return cnt + input / 5
        }
    }
    
    return -1
}

print(solution())
