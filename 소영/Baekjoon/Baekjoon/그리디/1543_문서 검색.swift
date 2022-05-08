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
  
  // 문서의 글자수가 찾아야하는 글자수보다 적다면 0 출력
  if document.count < search.count {
    print(count)
  } else {
    // document 시작점에서 search의 글자수만큼 잘라서 비교 시작
    var startIndex = document.startIndex
    var endIndex = document.index(startIndex, offsetBy: search.count)
    
    while true {
      // 비교했을 때 같다면
      if search == document[startIndex..<endIndex] {
        // 찾았으니 count 증가
        count += 1
        // 중복이 되면 안되므로 다음 시작 index를 이 문자열의 마지막 index로 지정
        startIndex = endIndex
        // 그 다음 endIndex가 범위를 넘어가지 않는지 체크 후 대입
        // 넘어간다면 break
        if let checkIndex = document.index(endIndex, offsetBy: search.count, limitedBy: document.endIndex) {
          endIndex = checkIndex
        } else {
          break
        }
      } else {
        // 비교 시 같지 않다면 그냥 다음 index로 넘어간다.
        // 마찬가지로 endIndex가 범위를 넘어가지 않는 지 체크 후 대입
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
