import Foundation

let input = readLine()!.split(separator: " ")
let N = Int(input[0])!
let k = input[1]
var result = 0
var currentHour : String
var currentMinute : String
var currentSecond : String
var currentTime : String
var flag : Bool = true


for hour in 0...N{
    if hour < 10 {
        currentHour = "0" + String(hour)
    }
    else {
        currentHour = String(hour)
    }
    
    for minute in 0...59{
        if minute < 10{
            currentMinute = "0" + String(minute)
        }
        else {
            currentMinute = String(minute)
        }
        
        for second in 0...59{
            if second < 10{
                currentSecond = "0" + String(second)
            }
            else{
                currentSecond = String(second)
            }
            currentTime = currentHour + currentMinute + currentSecond
            /*
            flag를 이용해 print 디버깅
            
            if (flag){
                print(currentTime)
            }
            flag = false
             */
            
            for digit in currentTime{
                if String(digit) == k{
                    result += 1
                    break
                }
            }
        }
    }
}

print(result)







