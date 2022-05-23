//
//  2941 크로아티아 알파벳.swift
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

func solved2941(){
    var count = 0
    let input = readLine()!
    var indicator = 0
    var character : String?
    while true{
        character = getCharacterByIndex(indicator, input: input)
        switch character
        {
        case "l":
            if getCharacterByIndex(indicator + 1, input: input) == "j"{
                indicator += 2
                count += 1
            }
            else {
                indicator += 1
                count += 1
            }
        
        case "n":
            if getCharacterByIndex(indicator + 1, input: input) == "j"{
                indicator += 2
                count += 1
            }
            else {
                indicator += 1
                count += 1
            }
        
        case "s":
            if getCharacterByIndex(indicator + 1, input: input) == "="{
                indicator += 2
                count += 1
            }
            else {
                indicator += 1
                count += 1
            }
            
        case "z":
            if getCharacterByIndex(indicator + 1, input: input) == "="{
                indicator += 2
                count += 1
            }
            else {
                indicator += 1
                count += 1
            }
        case "d":
            if getCharacterByIndex(indicator + 1, input: input) == "-"{
                indicator += 2
                count += 1
            }
            else if getCharacterByIndex(indicator + 1, input: input) == "z" && getCharacterByIndex(indicator + 2, input: input) == "="{
                indicator += 3
                count += 1
            }
            
            else {
                indicator += 1
                count += 1
            }
        case "c":
            if getCharacterByIndex(indicator + 1, input: input) == "="{
                indicator += 2
                count += 1
            }
            
            else if getCharacterByIndex(indicator + 1, input: input) == "-"{
                indicator += 2
                count += 1
            }
        
            
            else {
                indicator += 1
                count += 1
            }
            
        default:
            indicator += 1
            count += 1
        }
        
        if indicator >= input.count{
            break
        }
    }
    
    print(count)
    
}
