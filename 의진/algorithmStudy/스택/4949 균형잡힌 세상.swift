//
//  4949 균형잡힌 세상.swift
//  algorithmStudy
//
//  Created by 이의진 on 2022/05/23.
//

import Foundation
private struct Stack<T> {
    private var stack: [T] = []      값 (Immutable)/ 참조 (Mutable)  -> 깊은 복사, 얕은 복사    스위프트 구조체 vs 클래스 메서드 지원
    
    public var count: Int {
        return stack.count
    }
    
    public var isEmpty: Bool {
        return stack.isEmpty
    }
    
    public func getLastElement() -> T{
        return stack[stack.index(before: stack.endIndex)]
    }
    
    public mutating func push(_ element: T) {
        stack.append(element)
    }
    
    public mutating func pop() -> T? {
        return isEmpty ? nil : stack.popLast()
    }
}
func solved4949(){
    var results : [String] = []
    while true {
        let sentence : String
        var stack = Stack<Int>()
        var flag = true
        
        sentence = readLine()!
        if sentence == "."{
            break
        }
        
        for character in sentence{
            switch character
            {
            case "[":
                stack.push(1)
            case "]":
                if !stack.isEmpty && stack.getLastElement() == 1{
                    let _ = stack.pop()
                }
                else {
                    results.append("no")
                    flag = false
                }
            case "(":
                stack.push(2)
            case ")":
                if !stack.isEmpty && stack.getLastElement() == 2{
                    let _ = stack.pop()
                }
                else {
                    results.append("no")
                    flag = false
                }
            default:
                break
            }
            
            if !flag {
                break
            }
        }
        if flag && !stack.isEmpty{
            flag = false
            results.append("no")
        }
        if flag{
            results.append("yes")
        }
    }
    
    for result in results {
        print(result)
    }
}
