from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())

l = 1 
base = (n, l) # n개의 물병, 1리터의 물

n_new = n
l_new = l
shop = 0

while True:
    cnt = shop
    while True: #자연수로 나누어지는데 까지 일단 물병 합침
        n_new = n_new/2
        l_new = l_new*2
        cnt += 1
        if n_new/2 == n_new//2: break

    if n_new == k: 
        

print(shop)



    