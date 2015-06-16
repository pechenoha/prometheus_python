import sys

print "********************"
print "Calculation of n^m"
print "********************"

while True:
	try:
		n = int(raw_input("n = "))
		break
	except ValueError:
		print "Ooops... error, | n | should be INT."

while True:
	try:
		m = int(raw_input("m = "))
		break
	except ValueError:
		print "Ooops... error, | m | should be INT."

res = n**m

print str(n) + "^" + str(m) + " = " + str(res)