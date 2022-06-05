var input = readLine()!
var cnt = 0

// 클로저에 대한 부분이 부족해서 구글링 후 사용
while input.count >= 2{
    count += 1
    input = String(input.map{Int(String($0))!}.reduce(0, +))
}
print(count)
if input == "3" || input== "6" || input== "9"{
    print("YES")
}else{
    print("NO")
}
