import Foundation

let n = Int(readLine()!)!

var weights: [Int] = []

for _ in 0..<n {
    weights.append(Int(readLine()!)!)
}


weights = weights.sorted { $0 >= $1 }

var total = 0

for i in 0..<weights.count {
    total = max(total, weights[i] * (i+1))
}

print(total)
