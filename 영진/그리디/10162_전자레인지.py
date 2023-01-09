T=int(input())

botton_times=[300,60,10]
botton=[0,0,0]

for i in range(len(botton_times)):
    if T%botton_times[2]==0:
        botton[i]=T//botton_times[i]       
        T=T%botton_times[i]
        print(botton[i],end=' ')
    elif T%botton_times[2]!=0:
        print(-1)
        break  


   
