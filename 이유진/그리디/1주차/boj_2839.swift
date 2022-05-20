//
//  boj2839.swift
//  Algorithm
//
//  Created by 이유진 on 2022/05/08.
//

//12ms,79805KB
import Foundation

if let input = readLine() {
    let sugarWeight = Int(input)! //총 설탕무게
    var count = 0// 총 봉지 개수
    var restSugarWeight = 0//봉지에 담고 남은 설탕 무게 담을 변수
    
    //1.5kg봉지에 먼저 최대로 담고
    //2.남은 나머지들이 3kg 봉지로 나누어 떨어질 경우는 3kg로 나눠진 그 몫을 봉지 총개수(count)에 더해주고 break
    //3.남은 나머지들이 3kg 봉지로 나누어 떨어지지 않으면 5kg 봉지의 개수 하나 줄인 후 다시 계산
    restSugarWeight = sugarWeight//남은 설탕 무게 초기설정
    count = restSugarWeight / 5 //count는 5kg 봉지에 최대로 담았을때의 개수로 시작
    while(count > -1){
        restSugarWeight = sugarWeight - count*5// count 개수만큼의 5kg 봉지에 담은 후에 남는 설탕무게 계산
        if(restSugarWeight == 0){//남은 설탕이 없으면 반복문 break
            break;
        }else{//5kg에 담아주고 설탕이 남았을 경우 3kg봉지로 나누어 떨어지는지 확인
            if restSugarWeight % 3 == 0 {//나누어 떨어지는 경우 나눈 몫(3kg 봉지갯수)을 count에 추가로 더해주고 break
                count += restSugarWeight / 3
                break;
            }else{//나누어 떨어지지 않는 경우 5kg 봉지수를 하나 줄이고 다시 계산하기 위해 남은 설탕수 reset
                restSugarWeight = sugarWeight
                count -= 1
            }
        }
    }
    
    print(count)
    
}
