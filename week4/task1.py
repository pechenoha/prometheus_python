import sys

s = sys.argv[1].lower()
s = s.replace(" ", "")

s_reversed = s[::-1]

if s == s_reversed:
	result = "YES"
else:
	result = "NO"

print result