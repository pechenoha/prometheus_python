import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

result = None

if a + b > c and a + c > b and b + c > a:
	result = "triangle"
else:
	result = "not triangle"

print result
