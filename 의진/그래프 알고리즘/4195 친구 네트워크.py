import sys
input = sys.stdin.readline


def find(node):
    if node == graph[node]:
        return node
    graph[node] = find(graph[node])
    return graph[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        graph[root2] = root1
        cnt[root1] += cnt[root2]


# results = []
test_case = int(input())
for _ in range(test_case):
    graph = {}
    cnt = {}
    F = int(input())
    for _ in range(F):
        friend1, friend2 = input().rstrip().split()
        for friend in [friend1, friend2]:
            if friend not in graph:
                graph[friend] = friend
                cnt[friend] = 1
        union(friend1, friend2)
        print(cnt[find(friend1)])
# for result in results:
#     print(result)
