//
//  1026_보물.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/15.
//

func 보물() {
  let number = Int(readLine()!)!
  let aArray = readLine()!.split(separator: " ").map { Int($0)! }.sorted(by: <)
  let bArray = readLine()!.split(separator: " ").map { Int($0)! }.sorted(by: >)
  
  let min = (0..<number).reduce(0) { $0 + aArray[$1] * bArray[$1] }
  print(min)
}
