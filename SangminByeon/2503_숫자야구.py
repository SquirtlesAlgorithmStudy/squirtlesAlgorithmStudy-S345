from sys import stdin

is_answer = [True] * 1000

def hdr(n): return n//100
def ten(n): return (n%100)//10
def one(n): return n%10

for answer in range(123,988):
    if hdr(answer) == 0 or ten(answer) == 0 or one(answer) == 0:
        is_answer[answer] = False
    if hdr(answer) == ten(answer) or hdr(answer) == one(answer) or ten(answer) == one(answer):
        is_answer[answer] = False

n = int(stdin.readline().rstrip())

for _ in range(n):
    number, strike, ball = map(int,stdin.readline().rstrip().split())

    for answer in range(123,988):
        strike_cnt = 0
        ball_cnt = 0

        if is_answer[answer] == True:
            if hdr(answer) == hdr(number): strike_cnt += 1
            if hdr(answer) == ten(number) or hdr(answer) == one(number): ball_cnt += 1
                
            if ten(answer) == ten(number): strike_cnt += 1
            if ten(answer) == hdr(number) or ten(answer) == one(number): ball_cnt += 1

            if one(answer) == one(number): strike_cnt += 1
            if one(answer) == hdr(number) or one(answer) == ten(number): ball_cnt += 1


        if (strike, ball) != (strike_cnt, ball_cnt): is_answer[answer] = False

cnt = 0
for i in range(123,988):
    if is_answer[i]: cnt+=1

print(cnt)    