def rotation(wheel, direction):
   if direction == 1:  # 시계방향
     ref = [wheel[7]]
     wheel.pop()
     ref.extend(wheel)
     return ref

   elif direction == -1:  # 반시계방향
     last = wheel[0]
     del wheel[0]
     wheel.append(last)
     return wheel

 one_wheel = list(map(int,input()))
 two_wheel = list(map(int,input()))
 three_wheel = list(map(int,input()))
 four_wheel = list(map(int,input()))

 num = int(input())

 a=[0,0]

 for i in range(num):
   connection = [0,0,0]
   if one_wheel[2] != two_wheel[6]:
     connection[0] = 1
   if two_wheel[2] != three_wheel[6]:
     connection[1] = 1
   if three_wheel[2] != four_wheel[6]:
     connection[2] = 1

   a[0], a[1] = map(int, input().split())

   if a[0]==1:
     one_wheel=rotation(one_wheel,a[1])
     if connection[0]==1:
       two_wheel=rotation(two_wheel,-a[1])
     if connection[0]==1 and connection[1]==1:
       three_wheel=rotation(three_wheel,a[1])
     if connection[0]==1 and connection[1]==1 and connection[2]==1:
       four_wheel=rotation(four_wheel,-a[1])
   elif a[0]==2:
     two_wheel=rotation(two_wheel,a[1])
     if connection[0]==1:
       one_wheel=rotation(one_wheel,-a[1])
     if connection[1]==1:
       three_wheel=rotation(three_wheel,-a[1])
     if connection[1]==1 and connection[2]==1:
       four_wheel=rotation(four_wheel,a[1])
   elif a[0]==3:
     three_wheel=rotation(three_wheel,a[1])
     if connection[1]==1:
       two_wheel=rotation(two_wheel,-a[1])
     if connection[2]==1:
       four_wheel=rotation(four_wheel,-a[1])
     if connection[1]==1 and connection[0]==1:
       one_wheel=rotation(one_wheel,a[1])
   elif a[0] ==4:
     four_wheel=rotation(four_wheel,a[1])
     if connection[2]==1:
       three_wheel=rotation(three_wheel,-a[1])
     if connection[2]==1 and connection[1]==1:
       two_wheel=rotation(two_wheel,a[1])
     if connection[2]==1 and connection[1]==1 and connection[0]==1:
       one_wheel=rotation(one_wheel,-a[1])


 result=0
 score = [1,2,4,8]
 twclock=[one_wheel[0],two_wheel[0],three_wheel[0],four_wheel[0]]
 c=[x*y for x,y in zip(score,twclock)]
 for i in c:
   result+=i

 print(result)