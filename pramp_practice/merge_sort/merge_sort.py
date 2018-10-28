# merge sort
# Create algorithm for merge sort. The elements to
# be sorted must be of basic data types.
#

def merge_sort(e):
    if type(e) != list:
        raise TypeError

    if not all_elements_are_basic_data_types(e):
        raise ValueError

    size = len(e)

    if size == 0 or size == 1:
        return e

    low = 0
    high = size - 1

    perform_merge_sort(e, low, high)

    return e


def perform_merge_sort(e, low, high):
    if low >= high:
        return

    mid_point = (low + high) / 2

    perform_merge_sort(e, low, mid_point)
    perform_merge_sort(e, mid_point + 1, high)
    merge(e, low, mid_point, high)

def merge(e, low, mid, high):
    if low == mid and mid == high:
        return

    i = low
    j = mid + 1
    k = low

    temp = e[:]

    # compare and place the element of lower value to output
    while i <= mid and j <= high:
        if temp[i] <= temp[j]:
            e[k] = temp[i]
            i += 1
            k += 1
        else:
            e[k] = temp[j]
            j += 1
            k += 1

    # place remaining elements in either list to output
    while not finished_travelling(k, high):
        if i <= mid:
            e[k] = temp[i]
            i += 1
            k += 1

        if j <= high:
            e[k] = temp[j]
            j += 1
            k += 1

def finished_travelling(k, high):
    if k <= high:
        return False

    return True

def all_elements_are_basic_data_types(e):
    for item in e:
        if type(item) not in [bool, int, float, str]:
            return False

    return True
