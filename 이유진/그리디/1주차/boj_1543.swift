//
//  boj_1543.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/08.
//

//12ms,79504KB
import Foundation

var document = String()
var word = String()
if let input = readLine() {
    document = String(input)
}

if let input = readLine(){
    word = String(input)
}

var removedDocument = document.replacingOccurrences(of: word, with: "")
var result = (document.count-removedDocument.count) / word.count

print(result)
