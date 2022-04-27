import sys
fastin = sys.stdin.readline

n = int(fastin())
students = [list(fastin().rstrip().split()) for _ in range(n)]
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in students:
    print(student[0])
