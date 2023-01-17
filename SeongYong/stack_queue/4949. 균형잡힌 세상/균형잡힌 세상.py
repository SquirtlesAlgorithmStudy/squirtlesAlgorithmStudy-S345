

while(True):
	str = input()
	b_stack = []
	if str == '.':
		break
	
	for i in str:
		if i == '[' or i == '(':
			b_stack.append(i)
		elif i == ']':
			if len(b_stack) != 0 and b_stack[-1] == '[':
				b_stack.pop()
			else:
				b_stack.append(i)
				break
		elif i == ')':
			if len(b_stack) != 0 and b_stack[-1] == '(':
				b_stack.pop()
			else:
				b_stack.append(i)
				break
	
	if len(b_stack) == 0:
		print("yes")
	else:
		print("no")
