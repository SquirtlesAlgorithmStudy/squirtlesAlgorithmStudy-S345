//
//  2217_로프.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/15.
//

func 로프() {
  let number = Int(readLine()!)!
  let maxKgs: [Int] = (0..<number).map { _ in Int(readLine()!)! }.sorted(by: <)
  
  var maxValue = 0
  
  for (index, value) in maxKgs.enumerated() {
    if maxValue < value * (maxKgs.count - index) {
      maxValue = value * (maxKgs.count - index)
    }
  }
  print(maxValue)
}
