import sys

n = int(sys.argv[1])

for i in range (n+1):
	if i == 0:
		a_pr = 0
		a_current = 0
	else:
		if i == 1:
			a_current = 1
		else:
			temp = a_current
			a_current = a_current + a_pr
			a_pr = temp
print a_current

