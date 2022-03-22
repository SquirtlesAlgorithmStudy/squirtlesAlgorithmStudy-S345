#2주차 회의실 배정
import sys
fastin = sys.stdin.readline

stu_cnt = int(fastin())
students = []

for _ in range(stu_cnt):
  students.append(list(fastin().split())) 

students.sort(key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(stu_cnt):
  print(students[i][0])