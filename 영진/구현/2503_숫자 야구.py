from sys import stdin

num_of_question=int(input())

for _ in range(num_of_question):
    answer,num_of_strike,num_of_ball=map(int, stdin.readline().rstrip().split())

