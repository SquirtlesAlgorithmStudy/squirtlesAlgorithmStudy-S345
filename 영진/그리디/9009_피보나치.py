"""
range(start,end,step)
print(,end=" ") : " "안의 값을 바꿔 "\n"  대신에 사용할 수 있음
"""
T=int(input())
n=[]
for _ in range(T):
    n.append(input())
    

#첫째 항과 둘째 항 저장
fibonacci_numbers=[0,1]

# 피보나치 수열 생성
for i in range(2,100000):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

fibonacci_numbers.reverse()

for i in len(n):
    for j in fibonacci_numbers:
        n[i]=n[i]%j
        if i!=0:
            print(fibonacci_numbers[j])
        else:
            break
        





