import types as t

def is_unique(string):
	if type(string) != t.StringType:
		raise TypeError("The argument type must be string.")

	if string.rstrip() == "":
		raise ValueError("The arguement must be non-empty string")

	characters_in_ascii = [ord(x) for x in string]
	character_cnt = [0] * 128

	for x in characters_in_ascii:
		# omit if the selecdted character represents space
		if x == 32:
			continue
		else:
			character_cnt[x] += 1

	for cnt in character_cnt:
		if cnt > 1:
			return False

	return True

