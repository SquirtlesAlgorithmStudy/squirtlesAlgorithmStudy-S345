#list comprehension1
array_0 = [i * i for i in range(1, 10)]

#list comprehension2
a = [1,2,4,3,4,5,5,5]
remove_set = [3, 5]
result = [i for i in a if i not in remove_set]




#get input by blank
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

#knowing the num of input
g,d,h = map(int, input().split())

#faster then input()
import sys
sys.stdin.readline().rstrip()

#output using f-string
ans = 7
print(f"the answer is {ans}")




#using globalg 
g = 0
def func():
    global g
    g += 1

# packing : returning N value
# unpacking : getting N value in N variables

#lambda expression 1
array = [('a', 50), ('b', 32), ('c', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

#lambda expression 2
list1 = [1,2,3,4,5]
list2 = [6,7,8,5,2]

result = map(lambda a, b: a+ b, list1, list2)
print(list(result))



