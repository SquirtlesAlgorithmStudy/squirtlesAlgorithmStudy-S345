//
//  1026 보물.swift
//  algorithmStudy
//
//  Created by 이의진 on 2022/05/16.
//

import Foundation
func solving(){
    let N = Int(readLine()!)!
    var A : [Int] = Array(readLine()!.split(separator: " ").map{Int($0)!})
    let B : [Int] = Array(readLine()!.split(separator: " ").map{Int($0)!})
    
    A.sort(by:<)
    let B_sorted = B.sorted(by:>)
    let result = (0..<N).reduce(0){$0 + A[$1] * B_sorted[$1]}
    
    print(result)

}
