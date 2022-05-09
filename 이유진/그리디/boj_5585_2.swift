//
//  boj5585_2.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/07.
//

//12ms
import Foundation

if let input = readLine() {
    let cost = Int(input)!
    var count = 0
    var change = 1000 - cost
    let coinSystem = [500,100,50,10,5,1]
    
    for coin in coinSystem{
        count += change/coin
        switch coin{
        case 1:
            print(count)
        default:
            change = change%coin
        }
    }

}

