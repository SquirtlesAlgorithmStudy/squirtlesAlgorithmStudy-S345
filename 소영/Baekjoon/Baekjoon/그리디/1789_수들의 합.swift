//
//  1789_수들의 합.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/03.
//

import Foundation

func 수들의_합() {
  var num: Int = Int(readLine()!)!
  var index: Int = 1
  while num >= index {
    num -= index
    index += 1
  }
  
  print(index - 1)
}
