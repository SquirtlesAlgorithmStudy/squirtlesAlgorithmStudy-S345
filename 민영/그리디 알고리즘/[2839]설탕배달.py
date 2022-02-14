rest = int(input())
count = 0

with3 = [ rest // 3, rest % 3 ];
with5 = [ rest // 5, rest % 5 ];
if with5[1] == 0 :
    count = with5[0]
elif rest > 2:
    for i in range(with5[0] , -1 ,-1 ):
        if (rest - 5 * i) % 3 == 0:
            count = i + (rest - 5 * i)//3
            break;
        elif i == 0:
            count = -1
else:
    count = -1

print(count)
