//
//  boj5585.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/07.
//

//8ms
import Foundation

if let input = readLine() {
    var cost = Int(input)! //입력받은 가격
    var count = 0//동전 개수
    var change = 1000 - cost //거스름 받아야 하는 가격
    
    count += change/500
    change = change%500
    
    count += change/100
    change = change%100
    
    count += change/50
    change = change%50
    
    count += change/10
    change = change%10
    
    count += change/5
    change = change%5
    
    count += change/1
    
    print(count)
}
