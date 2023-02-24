//
//  14891 톱니바퀴.swift
//  algorithmStudy
//
//  Created by 이의진 on 2022/05/23.
//

import Foundation

private func getCharacterByIndex(_ index : Int, input : String) -> String?{
    if index < input.count {
        return String(input[input.index(input.startIndex, offsetBy: index)])
    }
    else {
        return nil
    }
}


private func circularShiftLeft(gears: [String],  gear: Int) -> String{
    var resultList = Array(repeating: "0", count: 8)
    let nowGear = gears[gear]
    for i in 1..<8{
        resultList[i-1] = getCharacterByIndex(i, input: nowGear)!
    }
    resultList[7] = getCharacterByIndex(0, input: nowGear)!
    return resultList.joined(separator: "")
}


private func circularShiftRight(gears: [String],  gear: Int) -> String{
    var resultList = Array(repeating: "0", count: 8)
    let nowGear = gears[gear]
    for i in 0..<7{
        resultList[i+1] = getCharacterByIndex(i, input: nowGear)!
    }
    resultList[0] = getCharacterByIndex(7, input: nowGear)!
    return resultList.joined(separator: "")
}


private func circularShift(direction: Int, gears : [String], gear: Int) -> String{
    if direction == 1{
        return circularShiftRight(gears: gears, gear : gear)
    }
    else {
        return circularShiftLeft(gears: gears, gear : gear)
    }
}


private func getAttractInfo(gears: [String]) -> [Bool]{
    var attract : [Bool] = []
    for i in 0..<3{
        if getCharacterByIndex(2, input: gears[i]) != getCharacterByIndex(6, input: gears[i+1]){
            attract.append(true)
        }
        else {
            attract.append(false)
        }
    }
    return attract
}


private func rotateGears(command: (Int, Int), gears: inout [String]){
    let isAttract : [Bool] = getAttractInfo(gears: gears)
    if command.0 == 1{
        gears[0] = circularShift(direction: command.1, gears: gears, gear: 0)
        var i : Int = 0
        var direction : Int
        while true{
            if i == 3{
                break
            }
            
            if isAttract[i]{
                direction = lroundf(pow(Float(-1), Float(i+1))) * command.1
                gears[i+1] = circularShift(direction: direction, gears: gears, gear: i+1)
            }
            
            else {
                break
            }
            i += 1
        }
    }
    
    else if command.0 == 4{
        gears[3] = circularShift(direction: command.1, gears: gears, gear: 3)
        var i : Int = 2
        var direction : Int
        while true{
            if i == -1{
                break
            }
            
            if isAttract[i]{
                direction = lroundf(pow(Float(-1), Float(i+1))) * command.1
                gears[i] = circularShift(direction: direction, gears: gears, gear: i)
            }
            
            else {
                break
            }
            i -= 1
        }
    }
    
    else if command.0 == 2{
        gears[1] = circularShift(direction: command.1, gears: gears, gear: 1)
        var i : Int = 1
        var direction : Int
        while true{
            if i == 3{
                break
            }
            
            if isAttract[i]{
                direction = lroundf(pow(Float(-1), Float(i))) * command.1
                gears[i+1] = circularShift(direction: direction, gears: gears, gear: i+1)
            }
            
            else{
                break
            }
            i += 1
        }
        i = 0
        while true{
            if i == -1{
                break
            }
            
            if isAttract[i]{
                direction = lroundf(pow(Float(-1), Float(i+1))) * command.1
                gears[i] = circularShift(direction: direction, gears: gears, gear: i)
            }
            
            else{
                break
            }
            i -= 1
        }
    }
    
    else if command.0 == 3{
        gears[2] = circularShift(direction: command.1, gears: gears, gear: 2)
        var i : Int = 2
        var direction : Int
        while true{
            if i == 3{
                break
            }
            
            if isAttract[i]{
                direction = lroundf(pow(Float(-1), Float(i+1))) * command.1
                gears[i+1] = circularShift(direction: direction, gears: gears, gear: i+1)
            }
            
            else{
                break
            }
            i += 1
        }
        i = 1
        while true{
            if i == -1{
                break
            }
            
            if isAttract[i]{
                direction = lroundf(pow(Float(-1), Float(i))) * command.1
                gears[i] = circularShift(direction: direction, gears: gears, gear: i)
            }
            
            else{
                break
            }
            i -= 1
        }
    }
}

private func getScore(gears: [String]) -> Int{
    return (Int(getCharacterByIndex(0, input: gears[0])!)!) + (2 * Int(getCharacterByIndex(0, input: gears[1])!)!) + (4 * Int(getCharacterByIndex(0, input: gears[2])!)!) + (8 * Int(getCharacterByIndex(0, input: gears[3])!)!)
}
    
    
        

func solved14891(){
    var gears : [String] = [readLine()!, readLine()!, readLine()!, readLine()!]
    let K = Int(readLine()!)!
    
    var commands : [(Int, Int)] = []
    var element : [Int]
    for _ in 0..<K{
        element = readLine()!.split(separator: " ").map{Int(String($0))!}
        commands.append((element[0], element[1]))
    }
    
    for command in commands {
        rotateGears(command: command, gears: &gears)
    }
    print(getScore(gears: gears))
    

    
}
