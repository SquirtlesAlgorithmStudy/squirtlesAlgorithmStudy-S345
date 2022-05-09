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
  // 원래 숫자에서 1부터 차례대로 뺀다
  // 뺄 숫자보다 남아있는 값이 작으면 while문을 탈출한다.
  // ex) 1 2 3 4 5 6 7 // 8
  // 처음 값이 34 였다면 1~7의 합이 28이기 때문에 8을 더하지 못하고 탈출한다.
  // 대신 1 2 3 4 5 6 13 을 더하면 34가 된다.
  while num >= index {
    num -= index
    index += 1
  }

  // 여기서 탈출된 index의 값은 더하지 못한 번호의 수이기 때문에 1을 빼서 출력해준다.
  print(index - 1)
}
