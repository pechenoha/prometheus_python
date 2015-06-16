def clean_list(lst):

	result = []

	def in_list(a):
		for item in result:
			if type(item) == type(a) and item == a:
				return True
		return False

	for item in lst:
		if not in_list(item):
			result.append(item)

	return result

a = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
print clean_list(a)
print 1 == "1"