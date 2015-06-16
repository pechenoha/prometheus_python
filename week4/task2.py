import sys

args = sys.argv[1:]
result = ""
n = len(args)

for i in range(0, n):
	result = result + args[n-1-i]
	if i != n-1:
		result = result + " "
		
print result