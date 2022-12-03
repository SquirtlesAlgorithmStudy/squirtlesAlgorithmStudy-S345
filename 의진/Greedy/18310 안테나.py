import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))

houses.sort()


def calculate_distance(houses, antenna):
    distance = 0
    for house in houses:
        distance += abs(house - antenna)
    return distance


if len(houses) % 2 == 1:
    print(houses[len(houses) // 2])

else:
    if calculate_distance(houses, houses[(len(houses) // 2) - 1]) <= calculate_distance(houses, houses[len(houses) // 2]):
        print(houses[(len(houses) // 2) - 1])
    else:
        print(houses[len(houses) // 2])
