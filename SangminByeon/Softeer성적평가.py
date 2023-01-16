from sys import stdin

n = int(stdin.readline().rstrip())

a_score = list(map(int,stdin.readline().rstrip().split()))
b_score = list(map(int,stdin.readline().rstrip().split()))
c_score = list(map(int,stdin.readline().rstrip().split()))
t_score = [a+b+c for a,b,c in zip(a_score,b_score,c_score)]

a_score_index = []
b_score_index = []
c_score_index = []
t_score_index = []


for i in range(n):
    a_score_index.append((a_score[i],i))
    b_score_index.append((b_score[i],i))
    c_score_index.append((c_score[i],i))
    t_score_index.append((t_score[i],i))

a_si_sorted = sorted(a_score_index, reverse=True)
b_si_sorted = sorted(b_score_index, reverse=True)
c_si_sorted = sorted(c_score_index, reverse=True)
t_si_sorted = sorted(t_score_index, reverse=True)

a_rank = [0 for _ in range(n)]
b_rank = [0 for _ in range(n)]
c_rank = [0 for _ in range(n)]
t_rank = [0 for _ in range(n)]


a_rank[a_si_sorted[0][1]] = 1
b_rank[b_si_sorted[0][1]] = 1
c_rank[c_si_sorted[0][1]] = 1
t_rank[t_si_sorted[0][1]] = 1

for rank in range(1,n):
    partA = a_si_sorted[rank][1]
    a_rank[partA] = rank+1
    if a_si_sorted[rank-1][0] == a_si_sorted[rank][0]:
        a_rank[partA] = a_rank[a_si_sorted[rank-1][1]]

    partB = b_si_sorted[rank][1]
    b_rank[partB] = rank+1
    if b_si_sorted[rank-1][0] == b_si_sorted[rank][0]:
        b_rank[partB] = b_rank[b_si_sorted[rank-1][1]]

    partC = c_si_sorted[rank][1]
    c_rank[partC] = rank+1
    if c_si_sorted[rank-1][0] == c_si_sorted[rank][0]:
        c_rank[partC] = c_rank[c_si_sorted[rank-1][1]]

    partT = t_si_sorted[rank][1]
    t_rank[partT] = rank+1
    if t_si_sorted[rank-1][0] == t_si_sorted[rank][0]:
        t_rank[partT] = t_rank[t_si_sorted[rank-1][1]]

print(*a_rank)
print(*b_rank)
print(*c_rank)
print(*t_rank)