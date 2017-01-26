def encrypt(text, rot):
	new_text = ""
	for character in text:
		new_text += rotate_character(character, rot)
	return new_text

def alphabet_position(letter):
	lc_alphabet = "abcdefghijklmnopqrstuvwxyz"
	uc_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for i in range(len(lc_alphabet)):
		if letter == lc_alphabet[i]:
			return i

	for i in range(len(uc_alphabet)):
		if letter == uc_alphabet[i]:
			return i


def rotate_character(char, rot):
	lc_alphabet = "abcdefghijklmnopqrstuvwxyz"
	uc_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	upper = False
	if char in uc_alphabet:
		upper = True

	#check if char is alpha
	if char.isalpha():
		#get index of char
		idx = alphabet_position(char)
		#rotate index rot times
		idx += rot
		while idx > 25:
			idx = idx % 26
		if upper:
			return uc_alphabet[idx]
		else:
			return lc_alphabet[idx]
	else:
		return char