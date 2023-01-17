from sys import stdin

nums = list(stdin.readline().rstrip().split('-'))

for i in range(len(nums)):
    try:
        nums[i] = eval(nums[i])
    except:
        znums = list(map(int,nums[i].split('+')))
        nums[i] = sum(znums)

sum = nums[0]

for i in range(1,len(nums)):
    sum -= nums[i]

print(sum)