//
//  1931_회의실 배정.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/16.
//

func 회의실_배정() {
  let num = Int(readLine()!)!
  var array = [[Int]]()
  var result = 0
  var startTime = 0
  
  (0..<num).forEach { _ in
    let temp = readLine()!.split(separator: " ").map { Int($0)! }
    array.append(temp)
  }
  
  array.sort(by: compare)
  
  (0..<num).forEach { i in
    if array[i][0] >= startTime {
      result += 1
      startTime = array[i][1]
    }
  }
  
  print(result)
  
  func compare (a: [Int], b: [Int]) -> Bool {
    if a[1] == b[1] {
      return a[0] < b[0]
    } else { return a[1] < b[1] }
  }
}
