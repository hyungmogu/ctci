import types as t

def urlify(string, true_length_of_chars):

	if type(string) != t.StringType or type(true_length_of_chars) != t.IntType:
		raise TypeError("Operation stopped. The data type of one or more arg for this function is incorrect. Make sure they are of the form (<string>, <int>)")

	if string == "" or true_length_of_chars == 0:
		raise ValueError("Operation stopped. The input 'string' has empty value. Make sure the input 'true_length_of_chars' has value greater than 0, and the input 'string' is not empty.")

	splitted_string = [x for x in string]

	total_length = len(splitted_string)

	if total_length < true_length_of_chars:
		raise ValueError("Operation stopped. The value of the input 'true_length_of_chars' is smaller than the total length of characters in the input 'string'.")


	i = 0

	while i < true_length_of_chars:

		if splitted_string[i] == " ":
			splitted_string[i] = "%20"

		i += 1

	output = "".join(splitted_string)

	return output