import sys; input = sys.stdin.readline

width, length = map(int, input().split())

if width >= 3:
	if length >= 6:
		print(length - 2)
	elif length == 5:
		print(4)
	else:
		print(length)
		
elif width == 2:
	if length >= 7:
		print(4)
	elif length == 6 or length == 5:
		print(3)
	elif length == 3 or length == 4:
		print(2)
	else:
		print(1)
		
else:
	print(1)
