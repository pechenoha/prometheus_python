def count_holes(n):

	n = str(n)
	if n != "" and (n.isdigit() or n[0] == "-" and n[1:].isdigit()):
		n = int(n)
	else:
		return "ERROR"

	number_h = {
		'-': 0,
		'0': 1,
		'1': 0,
		'2': 0,
		'3': 0,
		'4': 1,
		'5': 0,
		'6': 1,
		'7': 0,
		'8': 2,
		'9': 1,
	}

	result = 0;

	for key in str(n):
		result += number_h[key]

	return result

print count_holes('123')
print count_holes(906)
print count_holes('001')
print count_holes(-8)
print count_holes(-8.0)