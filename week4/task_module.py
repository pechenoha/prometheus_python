import sys

s = sys.argv[1].replace(" ", "")

alphabet = "abcdefghijklmnopqrstuvwxyz"
key      = "aaaaabbbbbabbbaabbababbaaababaab"
result   = ""
i = 0
j = 0
code = []

for ch in s:
	if j == 0:
		code.append("")

	if ch == ch.upper():
		code_ch = "b"
	else:
		code_ch = "a"
	code[i] = code[i] + code_ch

	# j - number of chars in string
	j = j + 1
	if j == 5:
		# jump to the next string
		j = 0
		i = i + 1

# if code[i] exists and it's length is lower than 5
if j > 0:
	code.pop(i)

for s in code:
	number = key.find(s)
	result = result + alphabet[number]

print result