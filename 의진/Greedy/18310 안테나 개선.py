import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))

houses.sort()

print(houses[(len(houses) - 1) // 2])
