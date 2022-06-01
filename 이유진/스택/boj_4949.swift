//
//  boj_4949.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/23.
//

import Foundation

struct Stack<T> {
    private var stack: [T] = []
    
    public var count: Int {
        return stack.count
    }
    public func peak() -> T? {
        return self.stack.last
        }
    
    public var isEmpty: Bool {
        return stack.isEmpty
    }
    
    public mutating func push(_ element: T) {
        stack.append(element)
    }
    
    public mutating func pop() -> T? {
        return isEmpty ? nil : stack.popLast()
    }
}

var inputs = [String]()
var input = ""

while(true){
    input = readLine()!
    if (input == "."){
        break
    }
    inputs.append(input)
}
       
var N = inputs.count
var answers = [String]()

for i in 0...N-1{
    let sentence = inputs[i]
    let M = sentence.count
    
    var stack = Stack<Character>()
    var balanced = true
    
    for j in 0...M-1{
        switch sentence[j]{
        case "(":
            stack.push("(")
        case "[":
            stack.push("[")
        case ")":
            if(stack.peak() == "("){
                stack.pop()
            }else{
                balanced = false
                break
            }
        case "]":
            if(stack.peak() == "["){
                stack.pop()
            }else{
                balanced = false
                break
            }
        default:
            continue
            
        }
        }
    if stack.count > 0{
        balanced = false
    }
    switch balanced{
    case true:
        answers.append("yes")
    case false:
        answers.append("no")
    }
}

for i in 0...answers.count-1{
    print(answers[i])
}

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

