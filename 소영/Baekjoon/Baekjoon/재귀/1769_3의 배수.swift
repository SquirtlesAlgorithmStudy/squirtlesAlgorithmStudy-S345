//
//  1769_3의 배수.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/19.
//

func 삼의_배수() {
  var startNumber = String(readLine()!)
  var count = 0
  let checkArray = [1, 2, 4, 5, 7, 8]
  
  while startNumber.count != 1 {
    startNumber = addAllDigit(number: startNumber)
  }

  print(count)
  checkArray.contains(Int(startNumber)!) ? print("NO") : print("YES")

  func addAllDigit(number: String) -> String {
    count += 1
    return String(number.reduce(0) { $0 + Int(String($1))! })
  }
}
