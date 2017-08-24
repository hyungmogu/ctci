# Question:
# 	There are three types of edits that can be performed.
#	Insert a character, remove a character, or replace a character.
# 	Given two strings, write a function to check if there are
# 	one edit away.


import types as t

def one_away(str1, str2):

	if type(str1) != t.StringType or type(str2) != t.StringType:
		raise TypeError("Operation stopped. The type of both argbs must be string")

	if str1.rstrip() == "" or str2.rstrip() == "":
		raise ValueError("Operation stopped. The value of both args must be non-empty")

	char_cnt_str1 = count_characters([x for x in str1])
	char_cnt_str2 = count_characters([x for x in str2])

	num_of_abscent_chars = 0

	for x in char_cnt_str1:

		try:
			char_cnt_str2[x]

		except KeyError:
			num_of_abscent_chars += 1

			if num_of_abscent_chars > 1:
				return False
			else:
				continue

		if not (char_cnt_str2[x] + 1 == char_cnt_str1[x] or 
			char_cnt_str2[x] - 1 == char_cnt_str1[x] or 
			char_cnt_str1[x] == char_cnt_str2[x]):
			
			return False


	return True


def count_characters(arr_of_char):
	
	output = {}

	for x in arr_of_char:

		if type(x) != t.StringType:
			raise TypeError("Operation stopped. All elements in the arg must be string")

		try: 
			output[x] += 1

		except KeyError:
			output[x] = 1

	return output