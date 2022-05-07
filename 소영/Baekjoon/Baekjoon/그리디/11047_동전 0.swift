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
  let coins: [Int] = (0..<coinsCount).map { _ in Int(readLine()!)! }.reversed()
  var count: Int = 0
  
  for coin in coins {
    let howManyCoins = cost / coin
    
    if cost == 0 { break }
    count += howManyCoins
    cost -= coin * howManyCoins
  }
  print(count)
}
