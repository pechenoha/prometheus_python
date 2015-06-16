import sys

s = sys.argv[1]
stack = [] # stack, where indexes of all "("-items are stored
i = 0
correct = True

for ch in s:
	if ch == "(":
		stack.append(i) # push index of "(" to stack
	elif ch == ")" and len(stack):
		# if stack is not empty
		stack.pop()
	else: 
		# if stack is empty, there is no "(" in stack for current ")"
		correct = False
		break
	i = i + 1

# all is fine, there is no extra "(" of ")" characters
# length of stack is responsible for extra "("
# correct is responsible for extra ")"
if correct and len(stack) == 0:
	result = "YES"
else:
	result = "NO"

print result