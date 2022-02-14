string = input()
word = input()
count =0

while True :
    strlist = list(string)
    locate = string.find(word)
    
    if locate >= 0:
        strlist = strlist[locate + len(word):]
        string = "".join(strlist)
        strlist = list(string)
        locate = string.find(word)
        count +=1;
        continue

    else:
        break
    
print (count)
