//
//  18312_시각.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/16.
//

func 시각() {
  let read = readLine()!.split(separator: " ").map{ Int($0)! }
  let hour = read[0]
  let number = read[1]
  var count = 0

  for hour in 0...hour {
    for min in 0..<60 {
      for second in 0..<60 {
        if hour % 10 == number || hour / 10 == number ||
            min % 10 == number || min / 10 == number ||
            second % 10 == number || second / 10 == number {
          count += 1
        }
      }
    }
  }

  print(count)
}
