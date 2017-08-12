import types as t

def selection_sort(arr, size):

	if type(arr) != t.ListType or type(size) != t.IntType:
		raise TypeError("Operation stopped. First arg has to be array type and second arg has to be int")

	if arr:

		try:
			arr[1]
		except IndexError:
			return arr

		i = 0
		while i < size - 1:
			j = i + 1
			index_element_to_be_swapped = i
			index_smallest_element = j

			while j < size:
				if arr[j] < arr[index_smallest_element]:
					index_smallest_element = j

				j += 1

			if arr[index_smallest_element] < arr[index_element_to_be_swapped]:
				temp = arr[index_element_to_be_swapped]
				arr[index_element_to_be_swapped] = arr[index_smallest_element]
				arr[index_smallest_element] = temp

			i += 1

		return arr

	else:
		raise ValueError("Operation stopped. Array has to have at least one element.")