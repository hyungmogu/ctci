import types as t

def palindrome_permutation(string):

	if type(string) != t.StringType:
		raise TypeError("The type of arguement is incorrect")


	if string.rstrip() == "":
		raise ValueError("The value of arguement must be non-empty")

	character_count = {}
	splitted_string = [x for x in string]
	num_of_sym_w_odd_num_of_chars = 0

	for x in splitted_string:
		if x != " ":
			try:
				character_count[x] += 1
			except KeyError:
				character_count[x] = 1

	for x in character_count:
		if character_count[x]%2 == 1:
			num_of_sym_w_odd_num_of_chars += 1

		if num_of_sym_w_odd_num_of_chars == 2:
			return False

	return True