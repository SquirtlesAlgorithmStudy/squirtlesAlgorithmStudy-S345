//
//  1543_문서 검색.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/07.
//

func 문서_검색() {
  let document = readLine()!
  let search = readLine()!
  var count = 0
  
  if document.count < search.count {
    print(count)
  } else {
    var startIndex = document.startIndex
    var endIndex = document.index(startIndex, offsetBy: search.count)
    
    while true {
      if search == document[startIndex..<endIndex] {
        count += 1
        startIndex = endIndex
        if let checkIndex = document.index(endIndex, offsetBy: search.count, limitedBy: document.endIndex) {
          endIndex = checkIndex
        } else {
          break
        }
      } else {
        startIndex = document.index(startIndex, offsetBy: 1)
        if let checkIndex = document.index(endIndex, offsetBy: 1, limitedBy: document.endIndex) {
          endIndex = checkIndex
        } else {
          break
        }
      }
    }
    print(count)
  }
}
