def counter(a, b):

	str_a = str(a)
	str_b = str(b)

	result   = 0
	unique_b = ""

	for ch in str_b:
		if not ch in unique_b:
			unique_b += ch

	for ch in unique_b:
		if ch in str_a:
			result += 1

	return result

print counter(1233211, 12128)
print counter(12121212, 1456)
print counter(123, 45)
print counter(123, 312)
