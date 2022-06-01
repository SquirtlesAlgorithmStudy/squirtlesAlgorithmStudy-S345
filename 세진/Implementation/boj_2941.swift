//
//  main.swift
//  Implementation
//
//  Created by User on 2022/05/23.
//
// https://www.acmicpc.net/problem/2941

import Foundation

var input = Array(readLine()!)
var croatiaAlphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
var i = 0
var lastIndex = input.count - 1
var result = 0

func check(_ str: String) -> Bool {
    if  croatiaAlphabet.contains(str) { return true }
    return false
}

while i < input.count {
    if i < lastIndex - 1 && input[i] == "d"{
        if check("\(input[i])\(input[i+1])\(input[i+2])") {
            result += 1
            i += 3
            continue
        }
    }
    if i < lastIndex {
        if check("\(input[i])\(input[i+1])") {
            result += 1
            i += 2
            continue
        }
    }
    i += 1
    result += 1
}

print(result)
