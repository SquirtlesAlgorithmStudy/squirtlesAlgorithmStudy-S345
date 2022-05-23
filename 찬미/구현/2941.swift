import Foundation

// Foundation에 좋은 함수가 있는 것을 발견하였습니다
// replacingOccurrences 함수 사용
// self 중 of에 해당하는 문자열로 with로 변경할 때 사용하는 문자열 치환 메서드

var input = readLine()!
let croatia: [String] = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia {
    input = input.replacingOccurrences(of: i, with: "a")
}

var cnt = input.count
print(cnt)
