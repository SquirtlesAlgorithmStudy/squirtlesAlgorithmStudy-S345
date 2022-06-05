//
//  main.swift
//  algo
//
//  Created by 김민재 on 2022/05/23.
//

import Foundation

var input = ""

while true {
    input = readLine()!
    if input == "." { break }
    
    var stack: [Character] = []
    var balanceFlag = true
    
    for char in input {
        if char == "(" || char == "[" {
            stack.append(char)
        } else if char == ")" {
            if !stack.isEmpty && stack[stack.count-1] == "(" {
                stack.removeLast()
            } else {
                // stack이 비어있다
                balanceFlag = false
                break
            }
        } else if char == "]" {
            if !stack.isEmpty && stack[stack.count-1] == "[" {
                stack.removeLast()
            } else {
                balanceFlag = false
                break
            }
        }
    }
    
    if !stack.isEmpty || !balanceFlag {
        print("no")
    } else {
        print("yes")
    }
    
    
}
