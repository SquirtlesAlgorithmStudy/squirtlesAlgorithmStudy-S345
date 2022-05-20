//
//  boj_1789.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/08.
//

import Foundation
//12ms,79508KB

if let input = readLine() {
    var S = Int(input)!
    var sum = 0
    var i = 0
    var result = 0
    
    while(S >= sum){
        i+=1
        sum+=i
        
    }
    result = i-1
  print(result)
}
