T=int(input())

case=[]
for i in range(T):
    case.append(int(input()))

for i in range(T):
    Quarter=int(case[i]//25)
    Dime=case[i]%25//10
    Nickel=case[i]%25%10//5
    Penny=case[i]%25%10%5//1
    print(Quarter,Dime,Nickel,Penny)