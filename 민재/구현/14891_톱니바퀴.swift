//
//  14891_톱니바퀴.swift
//  algo
//
//  Created by 김민재 on 2022/05/23.
//

// 12시 방향이 첫번째 인덱스
import Foundation


var wheel: [[Int]] = []

// 맞닿는 왼쪽 부분
let leftPointIndex = 6
// 맞닿는 오른쪽 부분
let rightPointIndex = 2
// 전체 톱니바퀴 개수
let wheelCnt = 4

for _ in 0..<wheelCnt {
    // 2차원 배열로 wheel 저장
    let input = readLine()!.map {Int(String($0))!}
    wheel.append(input)
}

let rotateCnt = Int(readLine()!)!
for _ in 0..<rotateCnt {
    let input = readLine()!.split(separator: " ").map {Int($0)!}
    
    // 몇번째 톱니바퀴를 돌릴건지
    let wheelNum = input[0] - 1
    // 어느 방향으로?
    let rotateDirection = input[1]
    
    // 돌았는지 확인할 bool list
    var checkRotated = Array(repeating: false, count: wheelCnt)
    // 회전 시작
    rotate(wheelNum: wheelNum, checklist: &checkRotated, direction: rotateDirection)
}

var plus = 1
var answer = 0

// 1번째 : 1점, 2번째 : 2점, 3번째 : 4점, 4번째 : 8점 -> 거듭제곱
for i in 0..<wheelCnt {
    answer += wheel[i][0] * plus
    plus *= 2
}

print(answer)


// 함수는 stack 영역 -> 참조가 아닌 값 복사, 원하는 건 위에서 선언한 checklist를 그대로 쓰는 것
// inout 메모리주소값으로 값 참조 가능
func rotate(wheelNum: Int, checklist: inout [Bool], direction: Int) {
    checklist[wheelNum] = true
    
    // 다음 톱니바퀴 인덱스
    let nextIdx = wheelNum + 1
    // 이전 톱니바퀴 인덱스
    let beforeIdx = wheelNum - 1
    
    // 다음 인덱스가 범위내 & 아직 돌지 않은 톱니바퀴 & 맞닿아 있는 부분이 다를때
    if nextIdx < wheelCnt && !checklist[nextIdx] && wheel[wheelNum][rightPointIndex] != wheel[nextIdx][leftPointIndex] {
        rotate(wheelNum: nextIdx, checklist: &checklist, direction: -direction)
    }
    
    // 전 인덱스가 범위내 & 아직 돌지 않은 톱니바퀴 & 맞닿아 있는 부분이 다를때
    if beforeIdx >= 0 && !checklist[beforeIdx] && wheel[wheelNum][leftPointIndex] != wheel[beforeIdx][rightPointIndex] {
        rotate(wheelNum: beforeIdx, checklist: &checklist, direction: -direction)
    }
    
    
    if direction == -1 {
        // 반시계방향
        // 첫번째를 빼서 맨뒤로
        let tmp = wheel[wheelNum].removeFirst()
        wheel[wheelNum].append(tmp)
    } else {
        // 시계방향
        // 맨 뒤를 빼서 첫번째로
        let tmp = wheel[wheelNum].removeLast()
        wheel[wheelNum].insert(tmp, at: 0)
    }
}
