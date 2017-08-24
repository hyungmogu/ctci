import types as t


# This method merges two sorted arrays. This is a requirement for merge sort
def merge_arrays(arr1, arr2, size1, size2):
	if type(arr1) != t.ListType or type(arr2) != t.ListType:
		raise TypeError("The data type of arguements must be of the form (List, List, Int, Int)")

	if arr1 == [] or arr2 == []:
		raise ValueError("Both arrays must be non-empty")

	i = 0
	j = 0
	k = 0

	temp = [0] * (size1 + size2)

	while i < size1 and j < size2:

		if arr1[i] <= arr2[j]:
			temp[k] = arr1[i]
			k += 1
			i += 1
		else:
			temp[k] = arr2[j]
			k += 1 
			j += 1

	while i < size1:
		temp[k] = arr1[i]
		i += 1
		k += 1

	while j < size2:
		temp[k] = arr2[j]
		j += 1
		k += 1

	return temp