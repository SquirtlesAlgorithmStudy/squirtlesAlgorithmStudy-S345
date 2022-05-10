//
//  2839_설탕 배달.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/07.
//

func 설탕_배달() {
  let deliverKg: Int = Int(readLine()!)!
  // 5로 최대한 많이 배달을 하는 것이 목표
  // 5로 나눴을 때 나머지가 0, 1, 2, 3, 4 인 경우를 나누어서 생각했다.
  // 0인 경우에는 더 생각할 게 없고
  // 1인 경우에는 5를 하나 가져와서 6을 만든 후 3 2개로 나누어서 든다.
  // 2인 경우에는 5를 2개 가져와서 12를 만든 후 3 4개로 나누어서 든다.
  // 여기에서 5를 2개 가져오지 못한다면 (즉, 기존 무게가 7이라면) 배달 불가
  // 3인 경우에는 3 하나가 추가되는 것이므로 count에 1을 더하면 된다.
  // 4인 경우네는 5개 하나를 가져와서 9를 만든 후 3 3개로 나누어서 든다.
  
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
