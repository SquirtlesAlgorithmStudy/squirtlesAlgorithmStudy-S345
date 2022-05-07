//
//  2839_설탕 배달.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/07.
//

func 설탕_배달() {
  let deliverKg: Int = Int(readLine()!)!
  var count = deliverKg / 5
  switch deliverKg % 5 {
  case 0:
    break
  case 1:
    count += 1
  case 2:
    if deliverKg == 7 {
      count = -1
      break
    }
    count += 2
  case 3:
    count += 1
  case 4:
    if deliverKg == 4 {
      count = -1
      break
    }
    count += 2
  default:
    break
  }
  print(count)
}
