//
//  2941 크로아티아 알파벳.swift
//  Week3
//
//  Created by 김지현 on 2022/05/23.
//

import Foundation

var word = readLine()!
let croatiaAlphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

croatiaAlphabet.forEach { alphabet in
    
    word = word.replacingOccurrences(of: alphabet, with: "*")
}

print(word.count)

/*
 replacingOccurences
 -> self 중 of에 해당하는 문자열로 with로 변경할 때 사용하는 문자열치환 메서드
 
 크로아티아 알파벳 배열을 한바퀴 돌면서
 word 내에 alphabet에 해당하는 문자열을 만나면 임의의 *로 바꿔준다
 (어차피 총 개수를 구하는 것이기 때문에 한글자 아무거나로 바꿔도 됨)
 
 마지막에 개수를 셀 때엔 크로아티아 배열에 없는 알파벳은 이미 한글자이기 때문에 고려 x
 */
