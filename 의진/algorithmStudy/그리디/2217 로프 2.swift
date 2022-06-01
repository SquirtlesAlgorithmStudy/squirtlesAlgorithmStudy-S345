//
//  2217 로프.swift
//  swift
//
//  Created by 이의진 on 2022/05/16.
//

import Foundation
func solved2217(){
    let N = Int(readLine()!)!
    var ropes : [Int] = []

    for _ in 0...N-1 {
        ropes.append(Int(readLine()!)!)
    }
    
    ropes.sort(by: <)
    
    var max_value = 0
    
    for (idx, rope) in ropes.enumerated(){
        if max_value < rope * (ropes.count - idx){
            max_value = rope * (ropes.count - idx)
        }
    }
    
    print(max_value)

}
