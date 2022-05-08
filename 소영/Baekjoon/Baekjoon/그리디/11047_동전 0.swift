//
//  11047_동전 0.swift
//  Baekjoon
//
//  Created by ohtt on 2022/05/07.
//

func 동전_0() {
  let read = readLine()!.split(separator: " ").map{ Int($0)! }
  let coinsCount = read[0]
  var cost = read[1]
  // 큰 동전부터 체크하기 위해 reversed 시켜서 저장
  let coins: [Int] = (0..<coinsCount).map { _ in Int(readLine()!)! }.reversed()
  var count: Int = 0
  
  // 동전들을 순회하면서 남아있는 가치 내에서
  // 해당 동전의 개수를 최대한 많이 빼낼 수 있도록 한다. (큰 동전부터 순회함)
  // 남은 가치가 0이 되면 break
  for coin in coins {
    let howManyCoins = cost / coin
    
    if cost == 0 { break }
    count += howManyCoins
    cost -= coin * howManyCoins
  }
  print(count)
}
