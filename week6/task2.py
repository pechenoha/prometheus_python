def encode_morze(text):

	morse_code = {
			"A" : ".-", 
			"B" : "-...", 
			"C" : "-.-.", 
			"D" : "-..", 
			"E" : ".", 
			"F" : "..-.", 
			"G" : "--.", 
			"H" : "....", 
			"I" : "..", 
			"J" : ".---", 
			"K" : "-.-", 
			"L" : ".-..", 
			"M" : "--", 
			"N" : "-.", 
			"O" : "---", 
			"P" : ".--.", 
			"Q" : "--.-", 
			"R" : ".-.", 
			"S" : "...", 
			"T" : "-", 
			"U" : "..-", 
			"V" : "...-", 
			"W" : ".--", 
			"X" : "-..-", 
			"Y" : "-.--", 
			"Z" : "--.."
		}

	words = text.upper().split(" ")
	emptyWords = []

	for i in range(len(words)):
		if words[i] == "":
			emptyWords.insert(0, i)
	for item in emptyWords:
		del words[item]

	unknownLetters = []
	for i in range(len(words)):
		for j in range(len(words[i])):
			if not words[i][j] in morse_code:
				unknownLetters.insert(0, (i, j))
	for item in unknownLetters:
		i_word   = item[0]
		i_letter = item[1]
		words[i_word] = words[i_word][:i_letter] + words[i_word][i_letter+1:]
		if not len(words[i_word]):
			del words[i_word]

	result = ""
	for i in range(len(words)):
		print words[i]
		for letter in words[i]:
			result += morse_code.get(letter, "").replace(".", "^_").replace("-", "^^^_") + "__"
		result += "____"
	if result:
		result = result[:len(result)-7]
	return result

# encode_morze("Hello     Brave new  World!")
print encode_morze("123 12 23 e")