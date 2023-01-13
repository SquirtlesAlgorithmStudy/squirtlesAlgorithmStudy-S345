from sys import stdin

n = int(stdin.readline().rstrip())

time_table = []

for _ in range(n):
    begin_time, finish_time = map(int, stdin.readline().rstrip().split())
    time_table.append((begin_time, finish_time))

time_table = sorted(time_table, key=lambda a: a[0])
time_table = sorted(time_table, key=lambda a: a[1])

end_time = 0 #마지막으로 끝난 회의 시간
conut = 0

for bt, ft in time_table:
  if bt >= end_time:
    conut += 1
    end_time = ft

print(conut)