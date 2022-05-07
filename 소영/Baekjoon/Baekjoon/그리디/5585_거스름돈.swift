//
//  5585_거스름돈.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/07.
//


func 거스름돈() {
  let cost = Int(readLine()!)!
  var change = 1000 - cost
  var count: Int = 0
  while true {
    switch change {
    case ..<5:
      change -= 1
    case ..<10:
      change -= 5
    case ..<50:
      change -= 10
    case ...100:
      change -= 50
    case ..<500:
      change -= 100
    default:
      change -= 500
    }
    count += 1
    if change <= 0 {
      break
    }
  }
  print(count)
}

