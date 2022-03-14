def transNum (string, count):
    temp = 0

    if  len(string) > 1:
        count += 1
        for i in string:
            temp += int(i)
        transNum(str(temp), count) 
    
    else:
        print (count)
        if (int(string) % 3)== 0:
            print ("YES")
        else:
            print("NO")

    return 0

N = input()
transNum(N , 0)
