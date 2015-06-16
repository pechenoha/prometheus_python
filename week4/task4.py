import sys

def get_sum(s):
	sum = 0
	for ch in s:
		sum = sum + int(ch)
	return sum

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
counter = 0
results = []

for i in range(a1, a2+1):
	x = str(i)
	if len(x) > 3:
		x1 = x[:len(x)-3]
		x2 = x[-3:]
		sum1 = get_sum(x1)
		sum2 = get_sum(x2)
	else:
		sum1 = 0
		sum2 = get_sum(x)
	if sum1 == sum2:
		counter = counter + 1
		results.append(i)

print counter