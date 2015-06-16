def super_fibonacci(n, m):

	f = []

	for i in range(n):
		if i >= m:
			f.append(sum(f[-m:]))
		else:
			f.append(1)

	return f[n-1]
	
# testing
print super_fibonacci(2, 1)
print super_fibonacci(3, 5)
print super_fibonacci(8, 2)
print super_fibonacci(9, 3)