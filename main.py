dp = [1, 2]


def hello(dp):
    dp.append(1)
    return dp


a = hello(dp)
a.append(3)
print(dp)
