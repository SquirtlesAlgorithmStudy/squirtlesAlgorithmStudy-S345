//
//  2941_크로아티아 알파벳.swift
//  algo
//
//  Created by 김민재 on 2022/05/23.
//

import Foundation

let cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

var input = readLine()!

for i in cro {
    input = input.replacingOccurrences(of: i, with: "a")
}

print(input.count)
