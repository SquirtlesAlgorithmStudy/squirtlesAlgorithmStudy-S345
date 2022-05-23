//
//  1769 3의 배수.swift
//  algorithmStudy
//
//  Created by 이의진 on 2022/05/23.
//

import Foundation

var count = 0
func recursion(x : String){
    if x.count > 1{
        var sum = 0;
        for digit in x{
            sum += Int(String(digit))!
        }
        count += 1
        recursion(x : String(sum))
    }
    
    else{
        print(count)
        if (Int(x)! % 3 == 0){
            print("YES")
        }
        else {
            print("NO")
        }
        exit(0)
    }
}

func solving(){
    let x = readLine()!
    recursion(x: x)
}
