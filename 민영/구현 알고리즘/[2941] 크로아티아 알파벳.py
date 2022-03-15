import sys
fastin = sys.stdin.readline
import re

list1 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = fastin().rstrip()
count = 0
#print (string)
for i in list1:
    count += string.count(i)
    #print(string.count(i))
    string = re.sub(i," ",string)
    #print(string)
temp = string.replace(" ", "")
#print (temp)
count += len(temp)
print (count)
