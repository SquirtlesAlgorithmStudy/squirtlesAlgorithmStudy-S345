//
//  main.swift
//  Stack
//
//  Created by User on 2022/05/23.
//
//https://www.acmicpc.net/problem/4949

import Foundation

func check(_ input: String) -> Bool {
    var stack = [Character]()
    for char in input {
        if leftBrackets.contains(char) {
            stack.append(char)
        } else if rightBrackets.contains(char) {
            guard let lastChar = stack.last else { return false }
            if isPair(first: lastChar, second: char) {
                let _ = stack.popLast()
            } else { return false }
        }
    }

    if stack.count == 0 { return true }
    return false
}

func isPair(first: Character, second: Character) -> Bool {
    if first == "(" && second == ")" { return true }
    if first == "[" && second == "]" { return true }
    return false
}

var results = [String]()
let leftBrackets: [Character] = ["(", "["]
let rightBrackets: [Character] = [")", "]"]

while true {
    let input = readLine()!
    
    if input == "." {
        break
    }
    
    check(input) ? results.append("yes") : results.append("no")

}

for result in results { print(result) }
